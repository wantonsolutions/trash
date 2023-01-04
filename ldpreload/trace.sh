#
# Run sort with fltrace tool
# 

usage="\n
-h, --help \t\t this usage information message\n"

#Defaults
SCRIPT_DIR=`dirname "$0"`
TOOL_DIR="/home/ena/faults-analysis/tool"
BINFILE="main.out"

TOOL_ARGS=""
TOOL_ARGS="${TOOL_ARGS} LOCAL_MEMORY=500000"

#source ${ROOTDIR}/scripts/utils.sh

# parse cli
for i in "$@"
do
case $i in
    # -d|--debug)
    # DEBUG=1
    # CFLAGS="$CFLAGS -DDEBUG"
    # ;;

    -h | --help)
    echo -e $usage
    exit
    ;;

    *)                      # unknown option
    echo "Unkown Option: $i"
    echo -e $usage
    exit
    ;;
esac
done

# build sort
LIBS="${LIBS} -lpthread -lm"
CFLAGS="$CFLAGS -DMERGE_RDAHEAD=0"
CFLAGS="$CFLAGS -no-pie -fno-pie"   # symbols
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space #no ASLR

#compile line
#sort
#gcc main.c qsort_custom.c -D_GNU_SOURCE -Wall -O ${INC} ${LIBS} ${CFLAGS} ${LDFLAGS} -o ${BINFILE}

#print
echo "Compiling"
gcc helloworld.c -D_GNU_SOURCE -Wall -O ${INC} ${LIBS} ${CFLAGS} ${LDFLAGS} -o ${BINFILE}

#run
cmd="sudo LD_PRELOAD=${TOOL_DIR}/fltrace.so ${TOOL_ARGS} ./${BINFILE}"
echo $cmd
$cmd
