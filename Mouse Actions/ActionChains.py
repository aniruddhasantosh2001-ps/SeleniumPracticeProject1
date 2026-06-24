# Action Chains ----------
#1. Mouse Hover -----> move_to_element(element)
#2. Right Click -----> context_click(element)
#3. Double Click -----> double_click(element)
#4. Drag and Drop -----> drag_and_drop(source, target)
#5. Slider -----> drag_and_drop_by_offset(element, x, y)

# Page Scrolling ----------

#1. Scroll down page by pixel ----->
#       driver.execute_script("window.scrollBy(0,3000)","")
#       value=driver.execute_script("return window.pageYOffset;")
#       print("Number of pixels moved:", value)

#2. Scroll down page till the element is visible
#       element=driver.find_element(By.XPATH, "//tag[id='value'])
#       driver.execute_script("arguments[0].scrollIntoView();", element)
#       value=driver.execute_script("return window.pageYOffset;")
#       print("Number ofpixels moved:", value)

#3. Scroll down page till end
#       driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#       value=driver.execute_script("return window.pageYOffset;")
#       print("Number of pixels moved:", value)

#4. Scroll up to starting position
#       driver.execute_script("window.scrollBy(0, -document.body.scrollheight)")
#       value=driver.execute_script("return window.pageYOffset;")
#       print("Number of pixels moved:", value)