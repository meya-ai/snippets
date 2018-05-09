from meya import Component
from meya.cards import List, Element, Button


class CardComponent(Component):
    def start(self):
        # instantiate the card
        elements = []
        button = Button(text="Read wiki",
                        url="https://en.wikipedia.org/wiki/Romanesco_broccoli")
        default_action = Button(
            url="https://en.wikipedia.org/wiki/Romanesco_broccoli",
            webview_height_ratio="tall")
        element = Element(title="Romanesco broccoli",
                          subtitle="Fractals in nature",
                          image_url="http://i.imgur.com/9Qh3xZF.jpg",
                          buttons=[button],
                          default_action=default_action)

        elements.append(element)

        button = Button(text="See formation", action="more_snowflake")
        default_action = Button(
            url="https://en.wikipedia.org/wiki/Snowflake",
            webview_height_ratio="tall")
        element = Element(title="Snowflakes",
                          subtitle="Fractals in nature",
                          image_url="http://i.imgur.com/AjOFeBV.jpg",
                          buttons=[button],
                          default_action=default_action)

        elements.append(element)

        list_button = Button(text="Show me Mandlebrot", action="next")

        card = List(elements=elements,
                    top_element_style="compact",
                    buttons=[list_button])

        # create the message (note the `card` rather than `text`)
        message = self.create_message(card=card)

        # respond as you normally would
        return self.respond(message=message, action="next")
