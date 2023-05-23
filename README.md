# leader-election

Algoritma, düğümlerin birbirleriyle mesajlaşarak lideri seçtiği bir aşamalı algoritmadır. Her düğüm başlangıçta lider seçimi için bir seçim başlatabilir. Bir düğüm seçim başlattığında, diğer düğümlere 'ELECTION' mesajı gönderir ve diğer düğümler bu mesajı alır. Algoritma, düğümler arasında iletişim sağlayan bir `send_message` yöntemi kullanır. Mesajlar, ağ gecikmesini simüle etmek için bir süre beklettikten sonra alıcı düğümlere iletilir.

Düğümler `receive_message` yöntemiyle mesajları işler. Eğer bir düğüm 'ELECTION' mesajı alırsa, seçim başlatılmamışsa seçim başlatır ve mesajı diğer düğümlere ileterek seçimi yaymaya devam eder. Düğümler birbirlerinden 'LEADER' mesajı aldıklarında, liderin kim olduğunu belirler ve lider mesajını diğer düğümlere ileterek liderin bilgisini yaymaya devam eder.

Her düğümün bir liderin olup olmadığını kontrol etmek için `leader_id` ve `election_in_progress` değişkenleri kullanılır. Bir düğüm lider olarak seçildiğinde, `leader_id` değişkeni güncellenir ve diğer düğümlere lider mesajı gönderilir.

Ana programda, belirli bir düğümün seçimi başlatması için `start_election` yöntemi kullanılır. Bu yöntem, ilk düğüm tarafından çağrılır ve 'ELECTION' mesajını diğer düğümlere gönderir. Ardından, bir süre bekler ve lider belirlenmemişse kendini lider olarak ilan eder ve 'LEADER' mesajını diğer düğümlere gönderir.

Son olarak, her düğümün liderin kim olduğunu kontrol etmek için `leader_id` bilgisini yazdırırız.

Bu örnekte, her düğümün kendine özgü bir kimlik (`node_id`) ve toplam düğüm sayısı (`num_nodes`) olduğunu varsayıyoruz. Düğümler arasındaki iletişimi ve lider seçimini simüle etmek için bir süre bekletme (`time.sleep`) işlemi kullanılıyor.

