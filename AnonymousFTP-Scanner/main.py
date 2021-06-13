import ftplib

def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous')
        print('\n [1] - ' + str(hostname) + ' FTP Anonymous Login Successful')
        ftp.quit()
        return True
    except Exception:
        print('\n [0] - ' + str(hostname) + ' FTP Anonymous Login Failed')
        return False

if __name__ == '__main__':
    anonLogin('90.130.70.73')