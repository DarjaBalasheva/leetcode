from style.base_style import font
from style.base_style import colors

# Стили дря лэйблов

total_label = {"anchor": 'ne',
               "background": colors.get("second_color"),
               "fg": colors.get("text_color_first"),
               "padx": 24,
               "pady": 24,
               "font": (font.get("main_font"),
                        font.get("second_font_size")),
               }

current_label = {"anchor": 'se',
                 "background": colors.get("second_color"),
                 "fg": colors.get("text_color_second"),
                 "padx": 24,
                 "pady": 24,
                 "font": (font.get("main_font"),
                          font.get("main_font_size"))
                 }
