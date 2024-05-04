{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3bdccd47",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "from random import seed\n",
    "from random import gauss\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6a41f922",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the Order: 8\n",
      "1\n",
      "0\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x576 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Generating Sequence\n",
    "def Hadamard(n):\n",
    "    H = np.full((n,n), True)\n",
    "\n",
    "\n",
    "    i1 = 1\n",
    "    integer = np.log2(n)\n",
    "    if round(integer)==integer:\n",
    "        while i1 < n:\n",
    "            for i2 in range(i1):\n",
    "                for i3 in range(i1):\n",
    "                    H[i2+i1][i3]    = H[i2][i3]\n",
    "                    H[i2][i3+i1]    = H[i2][i3]\n",
    "                    H[i2+i1][i3+i1] = not H[i2][i3]\n",
    "            i1 += i1\n",
    "\n",
    "        # Write the matrix.\n",
    "        for i in range(n):\n",
    "            for j in range(n):\n",
    "                if H[i][j]:\n",
    "                    H[i][j] = 1\n",
    "                else:\n",
    "                    H[i][j] = 0\n",
    "\n",
    "        H1 = H.astype(int)\n",
    "        return H1\n",
    "\n",
    "    else:\n",
    "        print(\"Enter n of power 2 please\")\n",
    "        \n",
    "#Dot Product of Two Rows        \n",
    "def dot_product(row1, row2):\n",
    "    #corr = np.zeros(math.factorial(n-1))\n",
    "    len_row1 = len(row1)\n",
    "    if len_row1==len(row2):\n",
    "        product = (np.dot(row1,row2))/len_row1\n",
    "        return product\n",
    "    else:\n",
    "        return none\n",
    "        \n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "#check_Orthogonality        \n",
    "def find_minimum(Hada):\n",
    "    n = Hada.shape[1] #length of the matrix\n",
    "    corr = 1000 #Creating the storage matrix for dot products\n",
    "    \n",
    "    \n",
    "    corr_index = np.zeros((2),int)\n",
    "    for i in range(n):\n",
    "        for j in range(i+1,n):\n",
    "            product = dot_product(Hada[i],Hada[j])\n",
    "            if product < corr:\n",
    "                corr = product\n",
    "                corr_index[0] = i\n",
    "                corr_index[1] = j\n",
    "                \n",
    "    i = corr_index[0]  \n",
    "    j = corr_index[1]\n",
    "    row_i = Hada[i]\n",
    "    row_j = Hada[j]\n",
    "    \n",
    "    return [row_i, row_j]\n",
    "\n",
    "def cdma_short(data, chips): #Short Code\n",
    "    ld = len(data)\n",
    "    lc = len(chips)\n",
    "    out = np.zeros(ld*lc)\n",
    "    i = 0\n",
    "    for d in data:\n",
    "        for c in chips:\n",
    "            out[i] = 1-(d+c)%2 #Unipolar Inverting\n",
    "            i += 1\n",
    "    return out\n",
    "\n",
    "data_length = 1000\n",
    "\n",
    "data1 = np.random.randint(0,2, data_length)\n",
    "data2 = np.random.randint(0,2, data_length)\n",
    "\n",
    "Hada = Hadamard(int(input(\"Enter the Order: \")))\n",
    "sequences = find_minimum(Hada)\n",
    "\n",
    "\n",
    "cdma_seq1 = cdma_short(data1,sequences[0])\n",
    "cdma_seq2 = cdma_short(data2,sequences[1])\n",
    "\n",
    "#---------- Parameter Settings -----------\n",
    "ovs = 32 #Oversampling Factor\n",
    "rate = 1e5 #Data Rate in Hz = 100 kHz\n",
    "\n",
    "data = [cdma_seq1,cdma_seq2] #Data Streams\n",
    "data_shift = [0,0] #Shift of Data Streams (Change Synchronization)\n",
    "\n",
    "\n",
    "#data = [[1,0,0,1,1,0],[1,0,0,1,1,0]] #Same Data Stream x2\n",
    "#data_shift = [0,int(ovs/2)] #Data Streams Offset 1/2 Bit Duration\n",
    "\n",
    "#TX\n",
    "P_max = 1 #LED Maximum Output Power\n",
    "TauOn = 2e-6 #Tau for Rising Edge in us\n",
    "TauOff = 1e-6 #Tau for Falling Edge in us\n",
    "\n",
    "#RX\n",
    "P_mindetect = 0.0 #Minimum Power which can be detected\n",
    "P_maxdetect = 5 #Maximum Power which can be detected (otherwise saturation)\n",
    "\n",
    "n_sigma = 0.01\n",
    "n_seed = 1\n",
    "#-----------------------------------------\n",
    "\n",
    "\n",
    "\n",
    "plt.figure(figsize=(10,8)) #Prepare Plot\n",
    "seed(n_seed) #Init Random Generator\n",
    "\n",
    "l = len(data[0])*ovs #Number of Samples\n",
    "out = np.zeros(l) #Output Vector for Final Result\n",
    "t = np.zeros(l) #Time Vector\n",
    "n = np.zeros(l) #Noise Vector\n",
    "dt = 1/(rate*ovs) #Duration of one Sample\n",
    "\n",
    "for i in range(l):\n",
    "    n[i] = gauss(0.0, n_sigma) #Generate Noise Samples\n",
    "    t[i] = dt*i #Set Time Markers for Plotting\n",
    "\n",
    "def run_led(d, shift=0, label=''):\n",
    "    P = 0\n",
    "    tmp_out = np.zeros(l)\n",
    "    for i in range(len(d)):\n",
    "        for j in range(ovs):\n",
    "            if d[i]: #Data = 1\n",
    "                P += (P_max - P) * (1-np.exp(-dt/TauOn))\n",
    "            else: #Data = 0\n",
    "                P *=  np.exp(-dt/TauOff);\n",
    "            tmp_out[(i*ovs)+j] = P\n",
    "    #print(tmp_out)\n",
    "    if shift:\n",
    "        tmp_out = np.roll(tmp_out, shift)\n",
    "    plt.plot(t, tmp_out, marker = '.', linestyle = '-', label = 'LED '+str(label))\n",
    "    return tmp_out\n",
    "    \n",
    "def show_plot():\n",
    "    plt.plot(t, out, marker = '+', linestyle = '-', label = 'RX Output')\n",
    "    plt.minorticks_on()\n",
    "    plt.ylabel('Output')\n",
    "    plt.xlabel('Time/s')\n",
    "    plt.legend(loc = 'upper right')\n",
    "    plt.grid(True)\n",
    "    plt.show()\n",
    "\n",
    "i = 0\n",
    "for d in data: #Process Data Stream and Sum-Up of Outputs\n",
    "    out += run_led(d, data_shift[i], i)\n",
    "    i += 1\n",
    "\n",
    "i = 0\n",
    "for o in out: #Clipping at Receiver Side\n",
    "    if o > P_maxdetect:\n",
    "        out[i] = P_maxdetect\n",
    "    elif o < P_mindetect:\n",
    "        out[i] = 0.0\n",
    "    i += 1\n",
    "out += n #Add Noise Vector\n",
    "\n",
    "def data_recover(chip_sequences, trans_data):\n",
    "    \n",
    "\n",
    "    stretch_seq0 = np.repeat(chip_sequences[0],ovs)\n",
    "    stretch_seq1 = np.repeat(chip_sequences[1],ovs)\n",
    "    loop_length = len(data1)\n",
    "    stretch_length = len(chip_sequences[0])*ovs\n",
    "\n",
    "    i = 0\n",
    "    j = stretch_length\n",
    "    threshold_value = .2915\n",
    "    data1_recovered = np.zeros(len(data1))\n",
    "    data2_recovered = np.zeros(len(data2))\n",
    "    l = 0\n",
    "\n",
    "    for k in range(loop_length):\n",
    "        user1_product = (np.dot(stretch_seq0,trans_data[i:j]))/stretch_length\n",
    "        user2_product = (np.dot(stretch_seq1,trans_data[i:j]))/stretch_length\n",
    "\n",
    "        if user1_product < threshold_value:\n",
    "            data1_recovered[l] = 0\n",
    "        else:\n",
    "            data1_recovered[l] = 1\n",
    "\n",
    "        if user2_product < threshold_value:\n",
    "            data2_recovered[l] = 0\n",
    "        else:\n",
    "            data2_recovered[l] = 1\n",
    "\n",
    "        l+=1\n",
    "        i = j\n",
    "        j+=stretch_length\n",
    "    return data1_recovered, data2_recovered\n",
    "    \n",
    "data_recovered1,data_recovered2 = data_recover(sequences,out)  \n",
    "\n",
    "#print(data_recovered1, data_recovered2)\n",
    "#print(data1,data2)\n",
    "print(np.count_nonzero(data_recovered1 != data1))\n",
    "print(np.count_nonzero(data_recovered2 != data2))\n",
    "\n",
    "show_plot()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
