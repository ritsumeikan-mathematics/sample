# %%
import re
def snake_to_camel(snake_str):
    components = snake_str.split('_')
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return components[0] + ''.join(x.title() for x in components[1:])

def camelToSnake(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

snake_str = "hello_world"
camelStr = snake_to_camel(snake_str)
snake_str2 = camelToSnake(camelStr)
print(f'{snake_str} -> {camelStr} -> {snake_str2}')

