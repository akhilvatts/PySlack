my_file = {
  'file' : (<pathToFile>, open(<pathToFile>, 'rb'), '<typeOfFile>')
}

payload={
  "filename":"<FileNameYouWishToShowInSlackMessage>.<ExtensionOfFile>", 
  "token":'<SlackToken>', 
  "channels":['#<SlackChannelName>'], 
}

r = requests.post("https://slack.com/api/files.upload", params=payload, files=my_file)
