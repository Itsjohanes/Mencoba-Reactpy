from reactpy import component, html, run

#component

@component
def Gallery(width, height):
    return html.img(
        {
            "src" : "https://picsum.photos/{width}/{height}",
            "alt" : "random image"
        }
    )
@component
def App():
    return html._(
        html.h1("Galeri menggunakan reactpy"),
        Gallery(width = 100, height = 200),
    

    )



run(App)