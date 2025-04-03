from nonebot.plugin import PluginMetadata, inherit_supported_adapters

from . import __main__ as __main__
from .config import Config

__version__ = "1.2.0"
__plugin_meta__ = PluginMetadata(
    name="白泽群管",
    description="基于山海经白泽神兽的群验证插件",
    usage="入群后，Bot 会发送验证问题，用户需私聊 Bot 回答正确答案才能通过验证。",
    type="application",
    homepage="https://github.com/afterow/nonebot-plugin-baize",
    config=Config,
    supported_adapters={"~onebot.v11"},
    extra={"License": "MIT", "Author": "afterow"}, # 补充 extra 信息
)
