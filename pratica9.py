from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel

def createTopology():
    net = Mininet()

    # Adicione hosts, switches e links à topologia
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    s1 = net.addSwitch('s1')

    net.addLink(h1, s1)
    net.addLink(h2, s1)

    # Inicialize a rede
    net.start()

    # Execute comandos personalizados na rede
    h1.cmd('ifconfig')
    h2.cmd('ping -c3 10.0.0.1')

    # CLI interativo para interagir com a topologia
    CLI(net)

    # Limpeza e encerramento da rede
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    createTopology()
