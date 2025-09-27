import asyncio
from time import sleep
import random
from telethon import events
from .client import client
from utils.logger import logger

@client.on(events.NewMessage(outgoing=True, pattern=r"^\.ping$"))
async def ping(event):
    logger.info("send pong")
    await event.edit("pong")

@client.on(events.NewMessage(outgoing=True, pattern=r"^\.help$"))
async def help(event):
    logger.info("send help")
    help_text = """
<b>Available Commands</b>:
<code>.help</code> — show this list of available commands
<code>.ping</code> — respond with pong
<code>.stop</code> — stop the userbot
<code>.slots &lt;number&gt;</code> — send a series of slot machine emojis
<code>.kit</code> — generate a random Minecraft PvP kit
<code>.DenysNazarenko</code> — fun animation command
<code>.hop</code> — display a Steve ASCII art
"""
    await event.reply(help_text, parse_mode='html')
    
@client.on(events.NewMessage(outgoing=True, pattern=r"^\.stop$"))
async def ping(event):
    logger.info("send stop")
    await event.edit("stopping...")
    await asyncio.sleep(0.5)
    await client.disconnect()
    
@client.on(events.NewMessage(outgoing=True, pattern=r"^\.slots (\d+)$"))
async def slots(event):
    logger.info("send slots")
    amount = int(event.pattern_match.group(1))
    interval = 1
    await  event.delete()
    for _ in range(amount):
        await event.respond("🎰\uFE0F")
        await asyncio.sleep(interval)
       

# Основное оружие
WEAPONS = [
    "Деревянный меч",
    "Каменный меч",
    "Железный меч",
    "Золотой меч",
    "Алмазный меч",
    "Незеритовый меч",
    "Деревянный топор",
    "Каменный топор", 
    "Железный топор",
    "Золотой топор",
    "Алмазный топор",
    "Незеритовый топор",
    " ",
]

# Доп. оружие
SECONDARY = [
    "Мотыга",
    "Деревянная лопата",
    "Каменная лопата",
    "Железная лопата",
    "Золотая лопата", 
    "Алмазная лопата",
    "Незеритовая лопата",
    "Трезубец",
    " ",
    "Деревянная кирка",
    "Каменная кирка",
    "Железная кирка", 
    "Золотая кирка",
    "Алмазная кирка",
    "Незеритовая кирка",
    "Кирка с зачарованием «Шёлковое касание»",

]

# Броня 
ARMOR_HELMETS = [
    "Кожаный шлем",
    "Железный шлем",
    "Алмазный шлем",
    " ",
]

ARMOR_CHESTS = [
    "Кожаный нагрудник",
    "Алмазный нагрудник",
    "Незеритовый нагрудник",
    " ",
]

ARMOR_LEGS = [
    "Кожаные поножи",
    "Железные поножи",
    " ",
]

ARMOR_BOOTS = [
    "Железные ботинки",
    "Алмазные ботинки",
    " ",
]

ENCHANTS = [
    "Острота II",
    "Прочность I",
    "Огненный аспект I",
    " ",
]

# Луки / арбалеты
BOWS = [
  "Лук",
    "Нагруженный лук",
    "Арбалет",
    "Тридент",
    "Снежок",
    "Яйцо призыва",
    " ",
]

# Стрелы
ARROWS = [
    # Обычные стрелы
    "1 стрела",
    "16 стрел",
    "32 стрелы", 
    "64 стрелы",
    "128 стрел",
    
    # Особые типы стрел
    "5 зачарованных стрел",
    "16 стрел яда",
    "8 стрел невидимости",
    "12 стрел замедления",
    "10 стрел урона",
    "3 стрелы лечебные",
    "7 огненных стрел",
    "6 стрел удачи",
    
    # Наборы и комбинации
    "Набор лучника (Лук + 32 стрелы)",
    "Колчан со смешанными стрелами",
    "Бесконечный лук + 1 стрела",
    "Арбалет с огненными стрелами",
    
    # Пустые слоты (как в инвентаре)
    " ",
    "[свободная ячейка]",
    "--пусто--",
]

# Зелья
POTIONS = [
    "Зелье силы",
    "Зелье скорости",
    "Зелье лечения",
    " ",
]

# Еда
FOOD = [
    "64 стейка",
    "64 золотых яблока",
    " ",
]

# Блоки
BLOCKS = [
    "64 обсидиана",
    "64 булыжника",
    " ",
]

# Разное
EXTRA = [
    "Эндэр-жемчуг",
    "Тотем бессмертия",
    " ",
]


@client.on(events.NewMessage(outgoing=True, pattern=r"^\.kit$"))
async def minecraft_kit(event):
    """Генератор PvP кита Minecraft"""

    weapon = random.choice(WEAPONS)
    secondary = random.choice(SECONDARY)
    helmet = random.choice(ARMOR_HELMETS)
    chest = random.choice(ARMOR_CHESTS)
    legs = random.choice(ARMOR_LEGS)
    boots = random.choice(ARMOR_BOOTS)
    enchant = random.choice(ENCHANTS)
    bow = random.choice(BOWS)
    arrows = random.choice(ARROWS)
    potion = random.choice(POTIONS)
    food = random.choice(FOOD)
    blocks = random.choice(BLOCKS)
    extra = random.choice(EXTRA)

    kit = f"""
🎮 Minecraft PvP Кит:
🗡 Оружие: {weapon} ({enchant})
⚔ Доп. оружие: {secondary}
🛡 Броня: {helmet}, {chest}, {legs}, {boots}
🏹 Дистанция: {bow} + {arrows}
🍷 Зелья: {potion}
🍖 Еда: {food}
🧱 Блоки: {blocks}
✨ Разное: {extra}
"""
    await event.edit(kit)


@client.on(events.NewMessage(outgoing=True, pattern=r"^\.DenysNazarenko$"))
async def _(event):
    await event.edit("`DIN DINNN.....`")
    await asyncio.sleep(1)
    await event.edit("`DINOOOOSAURUSSSSS!!`")
    await asyncio.sleep(1)
    await event.edit("`🏃                        🦖`")
    await event.edit("`🏃                       🦖`")
    await event.edit("`🏃                      🦖`")
    await event.edit("`🏃                     🦖`")
    await event.edit("`🏃   `LARII`          🦖`")
    await event.edit("`🏃                   🦖`")
    await event.edit("`🏃                  🦖`")
    await event.edit("`🏃                 🦖`")
    await event.edit("`🏃                🦖`")
    await event.edit("`🏃               🦖`")
    await event.edit("`🏃              🦖`")
    await event.edit("`🏃             🦖`")
    await event.edit("`🏃            🦖`")
    await event.edit("`🏃           🦖`")
    await event.edit("`🏃WOARGH!   🦖`")
    await event.edit("`🏃           🦖`")
    await event.edit("`🏃            🦖`")
    await event.edit("`🏃             🦖`")
    await event.edit("`🏃              🦖`")
    await event.edit("`🏃               🦖`")
    await event.edit("`🏃                🦖`")
    await event.edit("`🏃                 🦖`")
    await event.edit("`🏃                  🦖`")
    await event.edit("`🏃                   🦖`")
    await event.edit("`🏃                    🦖`")
    await event.edit("`🏃                     🦖`")
    await event.edit("`🏃  Huh-Huh           🦖`")
    await event.edit("`🏃                   🦖`")
    await event.edit("`🏃                  🦖`")
    await event.edit("`🏃                 🦖`")
    await event.edit("`🏃                🦖`")
    await event.edit("`🏃               🦖`")
    await event.edit("`🏃              🦖`")
    await event.edit("`🏃             🦖`")
    await event.edit("`🏃            🦖`")
    await event.edit("`🏃           🦖`")
    await event.edit("`🏃          🦖`")
    await event.edit("`🏃         🦖`")
    await event.edit("`DIA SEMAKIN MENDEKAT!!!`")
    await asyncio.sleep(1)
    await event.edit("`🏃       🦖`")
    await event.edit("`🏃      🦖`")
    await event.edit("`🏃     🦖`")
    await event.edit("`🏃    🦖`")
    await event.edit("`Dahlah Pasrah Aja`")
    await asyncio.sleep(1)
    await event.edit("`🧎🦖`")
    await asyncio.sleep(2)
    await event.edit("`-TAMAT-`")

@client.on(events.NewMessage(outgoing=True, pattern=r"^\.hop$"))
async def _(event):
    await event.edit(
"▬▬▬.◙.▬▬▬ \n"
"═▂▄▄▓▄▄▂ \n"
"◢◤ █▀▀████▄▄▄▄◢◤ \n"
"█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
"◥█████◤ \n"
"══╩══╩══ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ I am Steve :) \n"
"╬═╬☻/ \n"
"╬═╬/▌ \n"
"╬═╬/ \\ \n",
)