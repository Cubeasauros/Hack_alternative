import http_handle
import sys

send_data=http_handle.Wit('GVTH5PSJSWFGPUMUXB2NCFFQN2JLZTZ2')
out='ok'
if len(sys.argv) != 2:
	print('usage: python ' + sys.argv[0] + ' <wit-token>')
else:
	out=send_data.message(sys.argv[1])

print(out)



