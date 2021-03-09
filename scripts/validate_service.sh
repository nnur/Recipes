status=$(curl -s -o /dev/null -I -w "%{http_code}" http://localhost:8000)
echo "http status:  $status"
if [ $status = "200" ] ; then
    exit 0
else
    exit 1
fi