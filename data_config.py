class DataConfig:
    data_name = ""
    root_dir = ""
    label_transform = ""
    def get_data_config(self, data_name):
        self.data_name = data_name
        if data_name == 'LEVIR':
            self.label_transform = "norm"
            self.root_dir = './LEVIR-CD256/'
        elif data_name == 'NCC':
            self.label_transform = "norm"
            self.root_dir = '/EGY-Dataset/'
        elif data_name == 'quick_start_LEVIR':
            self.root_dir = './samples_LEVIR/'
     
        else:
            raise TypeError('%s not defined' % data_name)
        return self


if __name__ == '__main__':
    data = DataConfig().get_data_config(data_name='LEVIR')
    print(data.data_name)
    print(data.root_dir)
    print(data.label_transform)
