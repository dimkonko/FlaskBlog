import os

class OnlineCoderModel(object):
    def __init__(self):
        self.ace_path = "/home/dimkonko/FlaskBlog/static/js/libs/ace"
        self.themes_list = list()
        self.lang_list = list()

        self.init_all_lists()

    def init_all_lists(self):
        for file in os.listdir(self.ace_path):
        	cur_file = os.path.splitext(file)[0]

        	self.check_file(cur_file, self.themes_list, "theme")
        	self.check_file(cur_file, self.lang_list, "mode")

    def check_file(self, cur_file, list_to_load, data_type):
    	if cur_file.find(data_type) >= 0:
    		if cur_file.find("ext") < 0:
    			list_to_load.append(cur_file.split("-")[1])

    def get_themes_list(self):
    	return self.themes_list

    def get_lang_list(self):
    	return self.lang_list
