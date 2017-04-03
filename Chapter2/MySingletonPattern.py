class SecurityCameras(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not SecurityCameras._instance:
            SecurityCameras._instance = super(
                SecurityCameras, cls).__new__(cls, *args, **kwargs)
        return SecurityCameras._instance

    def __init__(self):
        self.security_cameras = []

    def add_cameras_building_1(self):
        for i in range(3):
            self.security_cameras.append('Video {} capture'.format(i+1))

    def add_cameras_building_2(self):
        self.security_cameras.pop()
        self.security_cameras.pop()
        self.security_cameras.append('Video 10 capture')
        self.security_cameras.append('Video 11 capture')


if __name__ == '__main__':
    building1 = SecurityCameras()
    building2 = SecurityCameras()

    building1.add_cameras_building_1()
    print 'checking cameras in building 1 \n'
    for i in building1.security_cameras:
        print ('security camera {}'.format(i))

    print 'checking cameras in building 2 \n'
    building2.add_cameras_building_2()
    for i in building2.security_cameras:
        print ('security camera {}'.format(i))
