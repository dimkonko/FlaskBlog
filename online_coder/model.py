import os

class OnlineCoderModel(object):
    def __init__(self):
        self.ace_path = "/home/dimkonko/FlaskBlog/static/js/libs/ace/"
        self.themes_list = list()
        self.lang_list = list()

        self.lang_ext_dict = {
            "javascript": "js",
            "python": "py",
            "textfile": "txt"
        }

        self.init_themes(self.ace_path + "themes")
        self.init_modes(self.ace_path + "modes")

    def init_themes(self, path):
        for file in os.listdir(path):
        	cur_file = os.path.splitext(file)[0]
        	self.themes_list.append(cur_file.split("-")[1])

    def init_modes(self, path):
        def find_ext(lang):
            for key in self.lang_ext_dict:
                if key == lang:
                    return self.lang_ext_dict[key]

        for file in os.listdir(path):
            cur_file = os.path.splitext(file)[0]
            file_name = cur_file.split("-")[1]

            lang_ext = find_ext(file_name)
            if not lang_ext:
                lang_ext = file_name

            self.lang_list.append({
		            "lang": file_name.capitalize(),
		            "lang_ext": lang_ext
            })

    def get_themes_list(self):
    	return self.themes_list

    def get_lang_list(self):
    	return self.lang_list
