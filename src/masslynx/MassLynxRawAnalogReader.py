import copy

import ctypes

from ctypes import*

from array import *

from .MassLynxRawReader import *
from .MassLynxRawDefs import MassLynxBaseType


class MassLynxRawAnalogReader(MassLynxRawReader):

    def __init__(self, source ):
        super().__init__(source, MassLynxBaseType.ANALOG)



    def ReadChannel( self, whichChannel ):
        times = []
        intensities = []

        # create the retrun values
        size = c_int(0)
        pTimes = c_void_p()
        pIntensities = c_void_p()


        # read tic
        readChannel = MassLynxRawReader.massLynxDll.readChannel
        readChannel.argtypes = [c_void_p, c_int, POINTER(c_void_p), POINTER(c_void_p), POINTER(c_int)]
        #readChannel(ptemp, whichChannel, pTimes, pIntensities, size)
        super().CheckReturnCode( readChannel(self._getReader(),whichChannel, pTimes, pIntensities, size))


        # fill the array
        pT = cast(pTimes,POINTER(c_float))
        pI = cast(pIntensities,POINTER(c_float))



        times = pT[0:size.value]
        intensities = pI[0:size.value]



        # dealocate memory

        return times, intensities