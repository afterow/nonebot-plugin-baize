from nonebot.plugin import PluginMetadata, inherit_supported_adapters

from . import __main__ as __main__
from .config import ConfigModel

__version__ = "0.1.0"
__plugin_meta__ = PluginMetadata(
    name="nonebot-plugin-baize",
    description="基于山海经白泽神兽的群验证插件",
    usage="入群后，Bot 会发送验证问题，用户需私聊 Bot 回答正确答案才能通过验证。",
    type="application",
    homepage="https://github.com/your-username/nonebot-plugin-baize",
    config=ConfigModel,
    supported_adapters=None,
)
