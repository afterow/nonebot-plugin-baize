# NoneBot2 群入群验证插件 (nonebot-plugin-baize)

一个基于 NoneBot2 的群入群验证插件，通过向新入群用户提问进行验证，防止机器人恶意刷群。**本版本已移除关键词匹配功能，只支持精确匹配。**

## 功能特性

*   **入群验证：** 新用户入群时，插件会自动发送验证问题到用户的私聊。
*   **题库管理：** 支持从 JSON 文件加载题库，方便管理和更新题目。
*   **精确答案验证：** 用户必须输入与答案完全一致的内容才能通过验证。
*   **超时自动移除：** 如果用户在指定时间内未通过验证，插件会自动将其从群中移除。
*   **灵活配置：**  通过配置文件可以自定义题库路径、超时时间等参数。

## 使用方法
## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-baize

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-baize
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-baize
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-baize
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-baize
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_template"]

</details>


## 贡献

欢迎提交 Pull Request 来改进本项目！

## License

[MIT](LICENSE)
