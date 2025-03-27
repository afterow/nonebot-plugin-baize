import asyncio
import json
from typing import Dict, Any
from nonebot import on_notice, on_message, get_driver
from nonebot.adapters.onebot.v11 import GroupIncreaseNoticeEvent, PrivateMessageEvent, Bot
from nonebot.params import EventPlainText
from nonebot.rule import is_type
from .config import Config

# 全局变量存储验证信息
verifying_users: Dict[int, Dict[str, Any]] = {}

# 加载配置
config: Config = Config.model_validate(get_driver().config.model_dump())

# 加载题库
try:
    with open(config.baize_question_path, "r", encoding="utf-8") as f:
        questions = json.load(f)
except FileNotFoundError:
    questions = []
    print(f"题库文件 {config.baize_question_path} 未找到，插件将无法正常工作！")
except json.JSONDecodeError:
    questions = []
    print(f"题库文件 {config.baize_question_path} JSON 格式错误，插件将无法正常工作！")

group_increase = on_notice(rule=is_type(GroupIncreaseNoticeEvent))


@group_increase.handle()
async def handle_group_increase(bot: Bot, event: GroupIncreaseNoticeEvent):
    global questions, verifying_users
    group_id = event.group_id
    user_id = event.user_id
    sub_type = event.sub_type  # 获取 sub_type 值

    if not questions:
        await group_increase.send(f"欢迎 {user_id} 加入本群，但是题库为空，无法进行验证！")
        return

    # 随机抽取一个问题
    import random

    question_data = random.choice(questions)
    question = question_data["question"]
    answer = question_data["answer"]

    # 将问题发送到群组
    await group_increase.send(f"欢迎 {user_id} 加入本群！请私聊我回答以下问题进行验证(回答不出会被踢哦)：\n{question}")

    # 记录验证信息
    verifying_users[user_id] = {
        "group_id": group_id,
        "question": question,
        "answer": answer,
        "timestamp": asyncio.get_event_loop().time(),
        "sub_type": sub_type,  # 记录 sub_type 值
        "bot": bot,  # 存储 bot 实例
    }

    # 设置超时，并直接在handle_group_increase中处理超时逻辑
    async def remove_user_after_timeout(user_id: int, timeout: int):
        await asyncio.sleep(timeout)
        if user_id in verifying_users:
            group_id = verifying_users[user_id]["group_id"]
            bot = verifying_users[user_id]["bot"]  # 获取 bot 实例
            del verifying_users[user_id]
            print(f"用户 {user_id} 验证超时，开始移除。")
            # 可以在这里执行踢出群组等操作
            try:
                await bot.set_group_kick(
                    group_id=group_id, user_id=user_id,
                )
                print(f"用户 {user_id} 验证超时，已从群 {group_id} 踢出。")
            except Exception as e:
                print(f"踢出用户 {user_id} 失败: {e}")

    asyncio.create_task(remove_user_after_timeout(user_id, config.baize_verify_timeout))


private_message = on_message(rule=is_type(PrivateMessageEvent))


@private_message.handle()
async def handle_private_message(
    bot: Bot, event: PrivateMessageEvent, message: str = EventPlainText()
):
    global verifying_users, config
    user_id = event.user_id

    if user_id in verifying_users:
        group_id = verifying_users[user_id]["group_id"]
        correct_answer = verifying_users[user_id]["answer"]
        sub_type = verifying_users[user_id]["sub_type"]  # 获取 sub_type 值

        # 答案验证
        result = message == correct_answer

        if result:
            await private_message.send(f"验证通过！欢迎加入本群！")
            del verifying_users[user_id]
        else:
            await private_message.send("答案错误，请重新回答。")
    # 可以在这里添加其他私聊消息处理逻辑
