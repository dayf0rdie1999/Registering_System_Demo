from kivy.clock import Clock

def main():
    print("Let's begin hiding password process")


class Password_Management():
    def __init__(self,object_id = None):
        self.password_dict = {}
        self.uncrypted_password = ""
        self.object_id = object_id


    def get_object_id(self):
        return self.object_id

    def set_object_id(self, new_object_id):
        self.object_id = new_object_id

    def Hiding_Password_System(self):
        try:
            if self.object_id.focus is True:
                if len(self.object_id.text) < len(self.password_dict):
                    self.remove_key(len(self.password_dict), len(self.object_id.text));
                elif len(self.object_id.text) == 0 and len(self.password_dict) == 0:
                    pass
                elif len(self.object_id.text) == len(self.password_dict) and \
                        self.object_id.text[
                            len(self.object_id.text) - 1] == "*":
                    pass
                else:
                    for index in range(0, len(self.object_id.text)):
                        if self.object_id.text[index] != "*" and self.check_key(
                                index) is False:
                            self.add_key(key_to_add=index,
                                         value_to_add=self.object_id.text[index])
                            self.object_id.text = self.create_hidden_password_string(
                                index)

                        elif self.object_id.text[index] != "*" and self.check_key(
                                index) is True:
                            self.update_key(index, self.object_id.text[index])
                            self.object_id.text = self.create_hidden_password_string(
                                index)
            else:
                pass
        except:
            pass



    def create_hidden_password_string(self, index):
        hidden_password_string = ""
        for ___ in range(-1, index):
            hidden_password_string = hidden_password_string + "*"

        return hidden_password_string

    def update_key(self, key_for_update, value_to_update):
        self.password_dict[key_for_update] = value_to_update

    def remove_key(self, length_dictionary, length_text):
        for index in range(length_dictionary, length_text, -1):
            del self.password_dict[index - 1]

    def add_key(self, key_to_add, value_to_add):
        self.password_dict[key_to_add] = value_to_add

    def check_key(self, key_to_check):
        if key_to_check in self.password_dict:
            return True
        else:
            return False

    def return_uncrypted_password(self):
        self.uncrypted_password = ""
        for index in range(0, len(self.password_dict)):
            for key,value in self.password_dict.items():
                if index == key:
                    self.uncrypted_password = self.uncrypted_password + value
                else:
                    pass
        return self.uncrypted_password



if __name__ == "__main__":
    main()