from network.Callback import Callback
from network.NeuralNetwork import NeuralNetwork

from numpy import ndarray as ARRAY

class VerboseCallback(Callback):
    """
    Вывод информации об обучении на экран - этот модуль по умолчанию.

    Можно написать свой
    """
    def __init__(self):
        super(VerboseCallback, self).__init__(-1, -1, -1, -1)

    def post_trained_batch(self, net: NeuralNetwork, sub_X: ARRAY, y: ARRAY):
        loss = net.get_output().loss()
        print(f"[Epoch: {self._m_epoch_id}, batch: {self._m_batch_id}] -> Loss = {loss}")