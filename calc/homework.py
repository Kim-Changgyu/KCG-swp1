from cgi import parse_qs
from homework_template import html

def application(environ, start_response):
	d = parse_qs(environ["QUERY_STRING"])
	a = d.get("a", [""])[0]
	b = d.get("b", [""])[0]
	response_body = html
	if "" in [a, b]:
		response_body = html.replace("Message", "Please input the value.")
	else:
		a, b = int(a), int(b)
		response_body = html.replace("Message", "SUM(a+b) : {}, PRODUCT(a*b) : {}".format(a+b, a*b))
	start_response("200 OK", [("Content-Type", "text/html"), ("Content-Length", str(len(response_body)))])
	return [response_body]
		