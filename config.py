import datetime

# Show individuals detected
SHOW_PROCESSING_OUTPUT = False
# Show individuals detected
SHOW_DETECT = True
# Data presentation
DATA_PRESENT = False
# Check for restricted entry
RE_CHECK = False
# Restricted entry time
RE_START_TIME = datetime.time(0,0,0) 
RE_END_TIME = datetime.time(23,0,0)
# Check for social distance violation
SD_CHECK = False
# Threshold for distance violation
SOCIAL_DISTANCE = 50
# Threshold for human detection minumun confindence
MIN_CONF = 0.1
# Threshold for Non-maxima surpression
NMS_THRESH = 0.2

# Video Path
VIDEO_CONFIG = {
	"VIDEO_CAP" : "video/7.mp4",
	"IS_CAM" : False
}

# Load YOLOv3-tiny weights and config
YOLO_CONFIG = {
	"weightsPath" : "YOLOv4-tiny/yolov4-tiny.weights",
	"configPath" : "YOLOv4-tiny/yolov4-tiny.cfg"
}
