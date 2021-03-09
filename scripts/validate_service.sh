status=$(curl -s -o /dev/null -I -w "%{http_code}" http://ec2-3-141-29-82.us-east-2.compute.amazonaws.com:8000)
if [ $status = "200" ] ; then
    echo $status
    exit 0
else
    echo $status
    exit 1
fi