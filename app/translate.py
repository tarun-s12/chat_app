from googletrans import Translator
import asyncio

async def translate_text(text, target_language):
    async with Translator() as translator:
        result = await translator.translate(text, dest=target_language)   
        return result.text

