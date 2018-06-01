def logger(msg):
    def log_message():
        print("Log: ", msg)
    return log_message


log_hi = logger("Hi") # log_message function returned from logger func is assigned to log_hi variable here
# log_hi() # equivalent to calling log_message()


def html_tag(tag):
    def wrap_text(msg):
        print(f'<{tag}>{msg}</{tag}>')
    return wrap_text


print_h1 = html_tag('h1')
# print(print_h1)
print_h1("This is a headline")

print_h2 = html_tag('h2')
print_h2('This is another headline')

print_p = html_tag('p')
print_p('This is a paragraph')

