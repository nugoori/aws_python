import wordcloud as wc

text = "python 파이썬 test 데이터 user wordcloud"
wcText = wc.WordCloud(font_path="C:\\Windows\\Fonts\\맑은 고딕\\malgun.ttf",
                      background_color="darkblue",
                      stopwords=["test", "user"],
                      min_font_size=20,
                      max_font_size=50,
                      width=1000,
                      height=1000)
wcText.generate_from_text(text)
wcText.to_image().show()
wcText.to_file("test")