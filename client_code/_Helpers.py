from anvil.js.window import jQuery, window

temp_scroll_top = None
jquery_window = jQuery(window)

def get_scroll_pos():
  global temp_scroll_top
  temp_scroll_top = jquery_window.scrollTop()

def set_scroll_pos():
  jquery_window.scrollTop(temp_scroll_top)

    
def maintain_scroll_position(func):
  def wrap(*args, **kwargs):
    get_scroll_pos()
    res = func(*args, **kwargs)
    set_scroll_pos()
    return res
  return wrap