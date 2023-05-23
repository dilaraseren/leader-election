import etcd
import time

def leader_election():
    client = etcd.Client(host='localhost', port=2379)  # etcd sunucusuna bağlantı
    election_key = "/leader-election/"  # lider seçimi için kullanılacak anahtar

    while True:
        try:
            # Lider adayı olmak için anahtarı oluşturma
            client.write(election_key, "candidate", ttl=10, prevExist=False)

            # Lider seçimi için anahtarın durumunu kontrol etme
            while True:
                leader_key = client.read(election_key).value

                if leader_key == "leader":
                    print("Bu düğüm liderdir.")
                    # Liderlik görevlerini gerçekleştirme
                    time.sleep(5)  # Örnek olarak 5 saniye bekleyelim

                    # Liderlik görevinin sonlandırılması
                    client.delete(election_key)
                    print("Liderlik görevi sonlandırıldı.")
                    break

                elif leader_key != "candidate":
                    print("Liderlik adayı değil. Bekleniyor...")
                    time.sleep(1)  # Lider değişikliği kontrolü için 1 saniye bekleme

        except etcd.EtcdAlreadyExist:
            print("Başka bir düğüm liderlik adayı. Yeniden deneyin...")
            time.sleep(1)  # Lider adayı olduğunda tekrar denemek için 1 saniye bekleme

        except etcd.EtcdKeyNotFound:
            print("Liderlik anahtarı mevcut değil. Bekleniyor...")
            time.sleep(1)  # Liderlik anahtarının oluşturulması için 1 saniye bekleme

if __name__ == "__main__":
    leader_election()
