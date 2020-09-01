"""
Available Commands: .gf

 """

from telethon import events

import asyncio




@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 5

    animation_ttl = range(0, 21)

    input_str = event.pattern_match.group(1)

    if input_str == "gf":

        await event.edit(input_str)

        animation_chars = [
        
            "`Ruk jaa , Abhi teri GF ko Fuck karta hu `",
            "`Making your Gf warm ðŸ”¥`",
            "`Pressing her boobs ðŸ¤šðŸ˜˜`",
            "`Stimulating her pussyðŸ–•`",
            "`Fingering her pussy ðŸ’§ðŸ˜ðŸ‘… `",
            "`Asking her to taste my DICKðŸŒ`",
            "`Requested acceptedðŸ˜»ðŸ’‹, Ready to taste my DICKðŸŒ`",
            "`Getting her ready to fuck ðŸ‘€`",
            "`Your GF Is Ready To Fuck`",
            "`Fucking Your GFðŸ˜ˆðŸ˜ˆ\n\n\nYour GF's Pussy Get Red\nTrying new SEX position to make her Squirt\n\nAlmost Done. 0%\nâ–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’ `",
            "`Fucking Your GFðŸ˜ˆðŸ˜ˆ\n\n\nYour GF's Pussy Get White\nShe squirted like a showerðŸ’§ðŸ’¦ðŸ‘…\n\nAlmost Done..\n\nFucked Percentage... 4%\nâ–ˆâ–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’ `",
            "`Fucking Your GFðŸ˜ˆðŸ˜ˆ\n\n\nYour GF's Pussy Get Red\nDoing Extreme SEX with herðŸ‘„\n\nAlmost Done...\n\nFucked Percentage... 8%\nâ–ˆâ–ˆâ–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’ `",
            "`Fucking Your GFðŸ˜ˆðŸ˜ˆ\n\n\nYour GF's Pussy Get Red\nWarming her AssðŸ‘ to Fuck!ðŸ‘ðŸ‘\n\nAlmost Done....\n\nFucked Percentage... 20%\nâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’ `",
            "`Fucking Your GFðŸ˜ˆðŸ˜ˆ\n\n\nYour GF's ASSðŸ‘ Get Red\nInserted my PenisðŸŒ in her ASSðŸ‘\n\nAlmost Done.....\n\nFucked Percentage... 36%\nâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’ `",
            "`Fucking Your GFðŸ˜ˆðŸ˜ˆ\n\n\nYour GF's ASSðŸ‘ Get Red\ndoing extreme sex with her\n\nAlmost Done......\n\nFucked Percentage... 52%\nâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’â–’ `",
            "`Fucking Your GFðŸ˜ˆðŸ˜ˆ\n\n\nYour GF's BoobsðŸ¤šðŸ˜˜ are Awesome\nPressing her tight NipplesðŸ¤šðŸ‘€\n\nAlmost Done.......\n\nFucked Percentage... 84%\nâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–’â–’â–’â–’â–’â–’ `",
            "`Fucking Your GFðŸ˜ˆðŸ˜ˆ\n\n\nYour GF's Lips Get Horny\nDoing French Kiss with your GFðŸ‘„ðŸ’‹\n\nAlmost Done........\n\nFucked Percentage... 89%\nâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–’â–’â–’ `",
            "`Fucking Your GFðŸ˜ˆðŸ˜ˆ\n\n\nYour GF's BoobsðŸ¤šðŸ˜˜ are Awesome\nI am getting ready to cum in her MouthðŸ‘„\n\nAlmost Done.......\n\nFucked Percentage... 90%\nâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–’â–’â–’ `",
            "`Fucking Your GFðŸ˜ˆðŸ˜ˆ\n\n\nYour GF's BoobsðŸ¤šðŸ˜˜ are Awesome\nFinally, I have cummed in her MouthðŸ‘…ðŸ‘„\n\nAlmost Done.......\n\nFucked Percentage... 96%\nâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–’ `",
            "`Fucking Your GFðŸ˜ˆðŸ˜ˆ\n\n\nYour GF's is Awesome\nShe is Licking my DickðŸŒ in the Awesome WayâœŠðŸ¤›ðŸ¤›ðŸ‘…ðŸ‘„\n\nAlmost Done.......\n\nFucked Percentage... 100%\nâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆ `",
            "`Fucking Your GFðŸ˜ˆðŸ˜ˆ\n\n\nYour GF's ASSðŸ‘ Get Red\nCummed On her MouthðŸ‘…ðŸ‘„\n\nYour GF got Pleasure\n\nResult: Now I Have 1 More SEX Partner ðŸ‘ðŸ‘`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 100])
