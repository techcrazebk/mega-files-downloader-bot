import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

class Translation(object):
    START_TEXT = f"""<b>Hello there,</b>
    
I am a <b>Mega Link Downloader</b> bot ❤️💫!

Just send me your mega.nz file link and I will return the file or video to you!

🤓 I can set custom captions & custom thumbnails!

🤓 I can download links which are bigger than 1GB too!(Limit 1.5GB)

Press /help for more details!

More Bots 🤖: @BotsByBk
Channel 📢: @ChannelsByBk

🤓 <b>I am open source so you can make your own bot from here!👇</b>"""
    
    DOWNLOAD_START = "<b>Downloading to my server now 📥</b> \n\n<code>Please wait uploading will start as soon as possible😇...</code>"
    UPLOAD_START = "Uploading to Telegram now 📤..."
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS =  "Downloaded in <b>{}</b> seconds.\n\nUploaded in <b>{}</b> seconds.\n\n<b>Thanks For Using This Free Service</b>"
    SAVED_CUSTOM_THUMB_NAIL = "𝗖𝘂𝘀𝘁𝗼𝗺 𝗧𝗵𝘂𝗺𝗯𝗻𝗮𝗶𝗹 𝗜𝘀 𝗦𝗮𝘃𝗲𝗱. 𝗧𝗵𝗶𝘀 𝗜𝗺𝗮𝗴𝗲 𝗪𝗶𝗹𝗹 𝗕𝗲 𝗨𝘀𝗲𝗱 𝗜𝗻 𝗬𝗼𝘂𝗿 𝗡𝗲𝘅𝘁 𝗨𝗽𝗹𝗼𝗮𝗱𝘀 📁.\n\nIf you want to delete it send\n /deletethumbnail anytime!"
    DEL_ETED_CUSTOM_THUMB_NAIL = "𝗖𝘂𝘀𝘁𝗼𝗺 𝗧𝗵𝘂𝗺𝗯𝗻𝗮𝗶𝗹 𝗖𝗹𝗲𝗮𝗿𝗲𝗱 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 ❌.\nYou will now get an auto generated thumbnail for your video uploads!"

    HELP_USER = f"""<b><u>🍁Hi I am a Mega Link Downloader Bot.. 🍁</u></b>
 
<b><u>How to use this bot:-</u></b>

<b>Just Send me your mega.nz file link!</b>

<b>Important things:-</b> 

- For Now folder links are not supported.

- Your link should be valid(not expired or been removed) & should not be password protected/encrypted/private!

📌 <b>Custom Thumbnail:-</b> (This step is Optional)

🙃 If you want a custom thumbnail for your file send me a photo before sending the link!.
     
 <i>(It means it is not necessary to send an image to include as an thumbnail.
If you don't send a thumbnail the video/file will be uploaded with an auto genarated thumbnail from the video.
The thumbnail you send will be used for your next uploads!)</i>

🙃 Press /deletethumbnail if you want to delete the previously saved thumbnail.
(Then the video will be uploaded with an auto-genarated thumbnail!)

📌 <b>Special feature</b> :- <i>Set caption to any file you want!</i>

🙃 Select an uploaded file or video or forward me <b>Any Telegram File</b> and Just write the text you want to be on the file as a reply to the File by selecting it (as replying to a message😅) and the text you wrote will be attached as caption!😍

📌 Watch Tutorial Video:- https://neon.ly/tutorial-video

More Bots 🤖: @BotsByBk

<b>Note</b> :- Please send only those download links which are not bigger than 1GB! Due to telegram API limits I can't upload files which are bigger than 1.5GB so I will split such files and upload them to you!

✨ <b>I am open source so you can make your own bot from here!👇</b>"""
