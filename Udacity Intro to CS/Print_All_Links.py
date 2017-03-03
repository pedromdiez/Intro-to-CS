page = 'Hola amigo <a href="test1"> mas <a href="test2"> mas <a href="test3"> mas <a href="test4"> mas <a href="test5"> mas <a href="test6"> mas <a href="test7"> mas'

def get_next_target(page):
    start_link = page.find('a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"',start_link)
    end_quote = page.find('"',start_quote+1)
    url = page[start_quote + 1,end_quote]
    return url, end_quote

def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print url
            page = page(endpos:)
        else:
            break
