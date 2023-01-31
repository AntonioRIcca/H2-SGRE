import certifi
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest


class WikiReaderApp(MDApp):
    def build(self):
        self.title = 'Wikipedia Reader'
        self.theme_cls.primary_palette = 'Teal'
        self.theme_cls.primary_hue = '400'

        return Builder.load_file('test_2.kv')

    def normal_search_button(self):
        query = self.root.ids['mdtext'].text
        self.get_data(title=query)

        pass

    def random_search_button(self):
        endpoint = 'https://it.wikipedia.org/w/api.php?action=query&list=random&rnlimit=1&rnnamespace=0&format=json'
        self.root.ids['mdlab'].text = 'Caricamento in corso...'
        self.rs_request = UrlRequest(endpoint,
                                     on_success=self.get_data,
                                     ca_file=certifi.where())
        print(self.root.ids)

    def get_data(self, *args, title=None):
        if title == None:
            # print('args: ', args)
            # print(type(args))
            response = args[1]
            random_article = response['query']['random'][0]
            title = random_article['title']
        endpoint = f'https://it.wikipedia.org/w/api.php?prop=extracts&explaintext&exintro&format=json&action=query&' \
                   f'titles={title.replace(" ", "%20")}'
        self.rs_request = UrlRequest(endpoint,
                                     on_success=self.set_textarea,
                                     ca_file=certifi.where())
        pass

    def set_textarea(self, request, response):
        page_info=response['query']['pages']
        page_id = next(iter(page_info))
        page_title = page_info[page_id]['title']
        try:
            content = page_info[page_id]['extract']
        except KeyError:
            content = f'Ci Spiace, ma la ricerca "{page_title}" non ha prodotto risultati\n\nRiprova!'
        self.root.ids['mdlab'].text = f'{page_title}\n\n{content}'

        pass


WikiReaderApp().run()


# KV = '''
# Screen:
#
#     MDRectangleFlatButton
#         text: 'Hello Kivi World!'
#         pos_hint: {'center_x': 0.5, 'center_y': 0.5}
# '''
#
#
# class MainApp(MDApp):
#     def build(self):
#         self.title = 'Hello Kivy'
#         self.theme_cls.theme_style = 'Dark'
#         self.theme_cls.primary_palette = 'Red'
#
#         return Builder.load_string(KV)
#
#
# MainApp().run()
