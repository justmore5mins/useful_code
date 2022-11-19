from socket import gethostname,gethostbyname
import IPy as ipy
from speedtest_cli import Speedtest

class ip_operate:
    """
    It can get ip by socket,
    it can get your ip and get your ip is public or pravite
    """
    def get_ip():
        return (gethostbyname(gethostname()))
    def ip_state(Ip:str):
        ip = ipy.IP(Ip)
        iptype = ip.iptype
        return iptype

class web_test:
    def speedtest():
        """
        it's speed test by speedtest for python mod
        """
        spt = Speedtest

        best_server = spt.get_best_server
        download_speed = float(spt.download())/1024/1024/8
        upload_speed = float(spt.upload())/1024/1024/8
        
        if download_speed > 1024:
            download_speed = download_speed/1024
        if upload_speed > 1024:
            upload_speed = upload_speed/1024
        
        return download_speed,upload_speed