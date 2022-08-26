from threading import Thread
from time import sleep

from data_loggers_and_statistics.temperature_data_loggers import TemperatureDataLogger
from data_structures.Observable_List import Observable_List
from logger_and_messages.printing_messages import printMessage
from observer.Observer import Observer
from ovens.Ovens import Oven_I

from temperature.Thermometers import Thermometer_I
from temperature.Temperature_Profile_Runners import Tempearture_Profile_Runner

import statistics

class TCal(Thread, Observer):

    def __init__(self,
                 threadname="TCal",
                 temperature_profile=[],
                 oven=Oven_I,
                 delay=None,
                 multimeter = None,
                 results_file = None):
        """
        :param threadname: An str with the name of the thread.
        :param temperature_profile: A list of integers with
        the temperatures to be applied during the thermal calibration process.
        :param temperature_stabilization_criteria: A tuple with the parameters that define the criteria of the temperature
        stabilization (sampling_period_secs, number_of_samples_of_window, stdev, number_of_consequtive_windows).
        """
        self.temperature_profile_runner = Tempearture_Profile_Runner(temperature_profile,oven)
        self.temperature_profile = temperature_profile
        self.oven = oven
        self.delay = delay
        self.multimeter = multimeter
        self.results_file = results_file

        self.temperature_data_logger = TemperatureDataLogger("temperature_data_logger",
                                                             self.thermometer,
                                                             self.temperature_stabilization_criteria[0]
                                                             )
        event = Observable_List.LEN_IS_MULTIPLE_OF_EVENT + str(self.n_samples_of_window)
        samplingBufer_empty_event = Observable_List.LIST_IS_EMPTY_EVENT

        self.temperature_data_logger.sampling_buffer.addEvent(event)
        self.temperature_data_logger.sampling_buffer.addEvent(samplingBufer_empty_event)
        self.temperature_data_logger.sampling_buffer.register(event, self, self.samplingBuffer_lenIsMultipleOf_event_handler)
        self.temperature_data_logger.sampling_buffer.register(samplingBufer_empty_event, self, self.samplingBuffer_empty_handler)


        Thread.__init__(self, name=threadname)

    def run(self):
        printMessage("Starting Temperature Calibration Process", "*", "*")

        self.oven.start() #solo para simulacion del horno

        #lo siguiente deberia ser una serie de ciclos SDM hasta que lleguemos al final del temperature profile
        # S -> Source  = Update oven Sp
        # D -> Delay  = Esperar a que se de cierta condicion que puede ser dependiente del tiempo, sampling buffer, etc.
        # M -> Measure = Ejecutar una serie de medidas

        while (self.temperature_profile_runner.hasnext()):
            self.temperature_profile_runner.next()
            self.delay.execute()
            self.update_results(self.multimeter.measure())

        #self.oven.update_temperatureSP(self.temperature_profile[0])
        #self.temperature_data_logger.start()

    def samplingBuffer_lenIsMultipleOf_event_handler(self, message):

        print("Pausamos el temperature data logger")
        self.temperature_data_logger.pause()

        #calculate the stdev
        stdev = statistics.stdev(message)
        print("stdev = " + str(stdev))

        self.temperature_data_logger.resume()

    def samplingBuffer_empty_handler(self, message):
        print(message)