from service.ddns_service import DDNS
from utils.timer_task import TimerTask
from utils.config import Config

config = Config()

if __name__ == '__main__':
    ddns_config = config.get_ddns_config()
    ddns = DDNS(ddns_config["access_key_id"],
                ddns_config["access_key_secret"],
                ddns_config["domain_name"],
                ddns_config["rrkey_word"],
                ddns_config["rtype"])
    timer_task = TimerTask(int(ddns_config["interval"])*60, ddns.ddns)
    timer_task.do_start()




