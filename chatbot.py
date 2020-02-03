import http_handle
import sys

send_data=http_handle.Wit('K5JLXDPZDAQUI26ZPBHJZUHMCNX37H5J')
out='ok'
if len(sys.argv) != 2:
	print('usage: python ' + sys.argv[0] + ' <wit-token>')
else:
	out=send_data.message(sys.argv[1])

print(out)



