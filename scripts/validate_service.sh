status=$(curl -s -o /dev/null -I -w "%{http_code}" http://ec2-3-141-29-82.us-east-2.compute.amazonaws.com:8000)
echo "http status:  $status"
if [ $status = "200" ] ; then
    exit 0
else
    exit 1
fi