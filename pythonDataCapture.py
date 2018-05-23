import requests
class captureData:
	def __init__(self):
		self.url = "http://www.baidu.com"
		content = self.get_content(self.url)
		print(content[0:50])
		print("222")

	def get_content(self,url):
		content = requests.get(url)
		print(content.text)
		return content.text
captureData()