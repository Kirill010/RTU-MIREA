#include <iostream>
#include <algorithm>
#include <random>
#include <cmath>
#include <fstream>
#include <thread>
#include <time.h>
#include <windows.h>

/// �������� ���� �������������

using namespace std;

struct neuron /// ��������� ������
{
    double value; /// ��������
    double error; /// ������
    void act() /// ������� ���������
    {
        value - (1 / (1 + pow(2.71828, -value)));
    }
};

class network /// ������
{
public:
    int layers; /// ���������� �����
    neuron** neurons; /// ��������� ������ ������� (��������� �� ���������)
    double*** weights; /// ��������� ������ ����� (��������� �� ��������� �� ���������) 1 - ����; 2 - ����� �������; 3 - ����� �����
    int* size; /// ����� ��� ������������� �������
    int threadsNum = 1; /// ���������� �������

    double sigm_pro(double x)
    {
        if ((fabs(x - 1) < 1e-9) or (fabs(x) < 1e-9))
        {
            return 0.0;
        }
        double res = x * (1.0 - x);
        return res;
    }

    double predict(double x)
    {
        if (x >= 0.8)
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }

    void setLayersNotStudy(int n, int* p, string filename) /// ����� ��� ����, ����� ����������� ������ ��������� ��� ��������
    {
        ifstream fin(filename);
        srand(time(0));
        layers = n;
        neurons = new neuron * [n];
        weights = new double** [n - 1];
        size = new int[n];
        for (int i = 0; i < n; i++)
        {
            size[i] = p[i];
            neurons[i] = new neuron[p[i]];
            if (i < (n - 1))
            {
                weights[i] = new double* [p[i]];
                for (int j = 0; j < p[i]; j++)
                {
                    weights[i][j] = new double[p[i + 1]];
                    for (int k = 0; k < p[i + 1]; k++)
                    {
                        fin >> weights[i][j][k];
                    }
                }
            }
        }
    }

    void setLayers(int n, int* p) /// ���� �� ������� ������� 
    {
        srand(time(0)); /// ������������ ��������� �����
        layers = n;
        neurons = new neuron * [n];
        weights = new double** [n - 1];
        size = new int[n];
        for (int i = 0; i < n; i++)
        {
            size[i] = p[i];
            neurons[i] = new neuron[p[i]];
            if (i < (n - 1))
            {
                weights[i] = new double* [p[i]]; /// �������� ��������� ������ �����
                for (int j = 0; j < p[i]; j++)
                {
                    weights[i][j] = new double[p[i + 1]];
                    for (int k = 0; k < p[i + 1]; k++)
                    {
                        weights[i][j][k] = ((rand() % 100)) * 0.01 / size[i]; /// ������������ ��������� ����
                    }
                }
            }
        }
    }

    void set_input(double* p)
    {
        for (int i = 0; i < size[0]; i++)
        {
            neurons[0][i].value = p[i];
        }
    }

    void show() /// ���� ������ � ���������, ������� ������� ��������� ��������� ����
    {
        setlocale(0, "");
        cout << "���� ����������: " << thread::hardware_concurrency() << endl;
        cout << "��������� ���� ����� �����������: ";
        for (int i = 0; i < layers; i++)
        {
            cout << size[i];
            if (i < (layers - 1))
            {
                cout << " - ";
            }
        }
        cout << endl;
        for (int i = 0; i < layers; i++)
        {
            cout << "\n#���� " << i + 1 << "\n\n";
            for (int j = 0; j < size[i]; j++)
            {
                cout << "������ #" << j + 1 << ": \n";
                cout << "��������: " << neurons[i][j].value << endl;
                if (i < (layers - 1))
                {
                    cout << "����: \n";
                    for (int k = 0; k < size[i + 1]; k++)
                    {
                        cout << "#" << k + 1 << ": ";
                        cout << weights[i][j][k] << endl;
                    }
                }
            }
        }
    }

    void LayersCleaner(int LayerNumber, int start, int stop) /// ������ ��� ������� �����
    {
        srand(time(0));
        for (int i = start; i < stop; i++)
        {
            neurons[LayerNumber][i].value = 0;
        }
    }

    void ForwardFeeder(int LayerNumber, int start, int stop)
    {
        for (int j = start; j < stop; j++)
        {
            for (int k = 0; k < size[LayerNumber - 1]; k++)
            {
                neurons[LayerNumber][j].value += neurons[LayerNumber - 1][k].value * weights[LayerNumber - 1][k][j];
            }
            /// cout << "�� ���������: " << neurons[i][j].value << endl;
            neurons[LayerNumber][j].act();
        }
    }

    double ForwardFeed()
    {
        setlocale(0, "");
        /// cout << "Function ForwardFeed:\n";
        /// cout << "Threads: " << threadsNum << endl;
        for (int i = 1; i < layers; i++)
        {
            if (threadsNum == 1)
            {
                /// cout << "�������� ������� ���� 1-� �����...\n";
                thread th1([&]() {
                    LayersCleaner(i, 0, size[i]);
                    });
                th1.join();
            }
            if (threadsNum == 2)
            {
                /// cout << "�������� ������� ���� 2-�� ������...\n";
                thread th1([&]() {
                    LayersCleaner(i, 0, int(floor(size[i] / 2)));
                    });
                thread th2([&]() {
                    LayersCleaner(i, int(floor(size[i] / 2)), size[i]);
                    });
                th1.join();
                th2.join();
            }
            if (threadsNum == 4)
            {
                if (size[i] == 1)
                {
                    cout << "�������� ������� ���� 1-� �����...\n";
                    LayersCleaner(i, 0, size[i]);
                }
                if ((size[i] == 2) or (size[i] == 3))
                {
                    cout << "�������� ������� ���� 2-�� ������...\n";
                    thread th1([&]() {
                        LayersCleaner(i, 0, int(floor(size[i] / 2)));
                        });
                    thread th2([&]() {
                        LayersCleaner(i, int(floor(size[i] / 2)), size[i]);
                        });
                    th1.join();
                    th2.join();
                }
                if (size[i] >= 4)
                {
                    cout << "�������� ������� ���� 4-�� ������...\n";
                    int start1 = 0; int stop1 = int(size[i] / 4);
                    int start2 = int(size[i] / 4); int stop2 = int(size[i] / 2);
                    int start3 = int(size[i] / 2); int stop3 = int(size[i] - floor(size[i] / 4));
                    int start4 = int(size[i] - floor(size[i] / 4)); int stop4 = size[i];
                    thread th1([&]() {LayersCleaner(i, start1, stop1);  });
                    thread th2([&]() {LayersCleaner(i, start2, stop2);  });
                    thread th3([&]() {LayersCleaner(i, start3, stop3);  });
                    thread th4([&]() {LayersCleaner(i, start4, stop4);  });
                    th1.join();
                    th2.join();
                    th3.join();
                    th4.join();
                }
            }
            if (threadsNum == 1)
            {
                thread th1([&]() {
                    ForwardFeeder(i, 0, size[i]);
                    });
                th1.join();
            }
            if (threadsNum == 2)
            {
                thread th1([&]() {
                    ForwardFeeder(i, 0, int(floor(size[i] / 2)));
                    });
                thread th2([&]() {
                    ForwardFeeder(i, int(floor(size[i] / 2)), size[i]);
                    });
                th1.join();
                th2.join();
            }
            if (threadsNum == 4)
            {
                if ((size[i] == 2) or (size[i] == 3))
                {
                    thread th1([&]() {
                        ForwardFeeder(i, 0, int(floor(size[i] / 2)));
                        });
                    thread th2([&]() {
                        ForwardFeeder(i, int(floor(size[i] / 2)), size[i]);
                        });
                    th1.join();
                    th2.join();
                }
                if (size[i] >= 4)
                {
                    int start1 = 0; int stop1 = int(size[i] / 4);
                    int start2 = int(size[i] / 4); int stop2 = int(size[i] / 2);
                    int start3 = int(size[i] / 2); int stop3 = int(size[i] - floor(size[i] / 4));
                    int start4 = int(size[i] - floor(size[i] / 4)); int stop4 = size[i];
                    thread th1([&]() {ForwardFeeder(i, start1, stop1);  });
                    thread th2([&]() {ForwardFeeder(i, start2, stop2);  });
                    thread th3([&]() {ForwardFeeder(i, start3, stop3);  });
                    thread th4([&]() {ForwardFeeder(i, start4, stop4);  });
                    th1.join();
                    th2.join();
                    th3.join();
                    th4.join();
                }
            }
        }

        double max = 0;
        double prediction = 0;
        for (int i = 0; i < size[layers - 1]; i++)
        {
            if (neurons[layers - 1][i].value > max)
            {
                max = neurons[layers - 1][i].value;
                prediction = i;
            }
        }
        return prediction;
    }

    void ErrorCounter(int LayerNumber, int start, int stop, double prediction, double rresult, double lr) /// ������� ������ ������� �������
    {
        if (LayerNumber == (layers - 1))
        {
            for (int j = start; j < stop; j++)
            {
                if (j != int(rresult))
                {
                    neurons[LayerNumber][j].error = -(neurons[LayerNumber][j].value);
                }
                else
                {
                    neurons[LayerNumber][j].error = 1.0 - neurons[LayerNumber][j].value;
                }
            }
        }
        else
        {
            for (int j = start; j < stop; j++)
            {
                double error = 0.0;
                for (int k = 0; k < size[LayerNumber + 1]; k++)
                {
                    error += neurons[LayerNumber + 1][k].error * weights[LayerNumber][j][k];
                }
                neurons[LayerNumber][j].error = error;
            }
        }
    }

    void WeightUpdater(int start, int stop, int LayerNum, int lr) /// ������� ��������� ����
    {
        int i = LayerNum;
        for (int j = start; j < stop; j++)
        {
            for (int k = 0; k < size[i + 1]; k++)
            {
                weights[i][j][k] += lr * neurons[i + 1][k].error * sigm_pro(neurons[i + 1][k].value) * neurons[i][j].value;
            }
        }
    }

    void BackPropogation(double prediction, double rresult, double lr) /// ���� �� �������� �������
    {
        for (int i = (layers - 1); i > 0; i--)
        {
            if (threadsNum == 1)
            {
                if (i == (layers - 1))
                {
                    for (int j = 0; j < size[i]; j++)
                    {
                        if (j != int(rresult))
                        {
                            neurons[i][j].error = -(neurons[i][j].value);
                        }
                        else
                        {
                            neurons[i][j].error = 1.0 - neurons[i][j].value;
                        }
                    }
                }
                else
                {
                    for (int j = 0; j < size[i]; j++)
                    {
                        double error = 0.0;
                        for (int k = 0; k < size[i + 1]; k++)
                        {
                            error += neurons[i + 1][k].error * weights[i][j][k];
                        }
                        neurons[i][j].error = error;
                    }
                }
            }
            if (threadsNum == 2)
            {
                thread th1([&]() {
                    ErrorCounter(i, 0, int(size[i] / 2), prediction, rresult, lr);
                    });
                thread th2([&]() {
                    ErrorCounter(i, int(size[i] / 2), size[i], prediction, rresult, lr);
                    });
                th1.join();
                th2.join();
            }
            if (threadsNum == 4)
            {
                if (size[i] < 4)
                {
                    if (i == (layers - 1))
                    {
                        for (int j = 0; j < size[i]; j++)
                        {
                            if (j != int(rresult))
                            {
                                neurons[i][j].error = -(neurons[i][j].value);
                            }
                            else
                            {
                                neurons[i][j].error = 1.0 - neurons[i][j].value;
                            }
                        }
                    }
                    else
                    {
                        for (int j = 0; j < size[i]; j++)
                        {
                            double error = 0.0;
                            for (int k = 0; k < size[i + 1]; k++)
                            {
                                error += neurons[i + 1][k].error * weights[i][j][k];
                            }
                            neurons[i][j].error = error;
                        }
                    }
                }
                if (size[i] >= 4)
                {
                    int start1 = 0; int stop1 = int(size[i] / 4);
                    int start2 = int(size[i] / 4); int stop2 = int(size[i] / 2);
                    int start3 = int(size[i] / 2); int stop3 = int(size[i] - floor(size[i] / 4));
                    int start4 = int(size[i] - floor(size[i] / 4)); int stop4 = size[i];
                    thread th1([&]() {
                        ErrorCounter(i, start1, stop1, prediction, rresult, lr);
                        });
                    thread th2([&]() {
                        ErrorCounter(i, start2, stop2, prediction, rresult, lr);
                        });
                    thread th3([&]() {
                        ErrorCounter(i, start3, stop3, prediction, rresult, lr);
                        });
                    thread th4([&]() {
                        ErrorCounter(i, start4, stop4, prediction, rresult, lr);
                        });
                    th1.join();
                    th2.join(); 
                    th3.join();
                    th4.join();
                }
            }
        }
        for (int i = 0; i < (layers - 1); i++)
        {
            if (threadsNum == 1)
            {
                for (int j = 0; j < size[i]; j++)
                {
                    for (int k = 0; k < size[i + 1]; k++)
                    {
                        weights[i][j][k] += lr * neurons[i + 1][k].error * sigm_pro(neurons[i + 1][k].value) * neurons[i][j].value;
                    }
                }
            }
            if (threadsNum == 2)
            {
                thread th1([&]() {
                    WeightUpdater(0, int(size[i] / 2), i, lr);
                    });
                thread th2([&]() {
                    WeightUpdater(int(size[i] / 2), size[i], i, lr);
                    });
                th1.join();
                th2.join();
            }
            if (threadsNum == 4)
            {
                if (size[i] < 4)
                {
                    for (int j = 0; j < size[i]; j++)
                    {
                        for (int k = 0; k < size[i + 1]; k++)
                        {
                            weights[i][j][k] += lr * neurons[i + 1][k].error * sigm_pro(neurons[i + 1][k].value) * neurons[i][j].value;
                        }
                    }
                }
                if (size[i] >= 4)
                {
                    int start1 = 0; int stop1 = int(size[i] / 4);
                    int start2 = int(size[i] / 4); int stop2 = int(size[i] / 2);
                    int start3 = int(size[i] / 2); int stop3 = int(size[i] - floor(size[i] / 4));
                    int start4 = int(size[i] - floor(size[i] / 4)); int stop4 = size[i];
                    thread th1([&]() {
                        WeightUpdater(start1, stop1, i, lr);
                        });
                    thread th2([&]() {
                        WeightUpdater(start2, stop2, i, lr);
                        });
                    thread th3([&]() {
                        WeightUpdater(start3, stop3, i, lr);
                        });
                    thread th4([&]() {
                        WeightUpdater(start4, stop4, i, lr);
                        });
                    th1.join();
                    th2.join();
                    th3.join();
                    th4.join();
                }
            }
        }
    }

    bool SaveWeights()
    {
        ofstream fout("weights.txt");
        for (int i = 0; i < layers; i++)
        {
            if (i < (layers - 1))
            {
                for (int j = 0; j < size[i]; j++)
                { 
                    for (int k = 0; k < size[i + 1]; k++)
                    {
                        fout << weights[i][j][k] << " ";
                    }
                }
            }
        }
        fout.close(); /// ��������� ����
        return 1;
    }

};

int main()
{
    srand(time(0));
    setlocale(0, "");
    ifstream fin;
    ofstream fout;
    const int l = 4; /// ���������� ����� � ��� �����
    const int input_l = 4096; /// 64 ** 2 ��������� � �������� 64*64
    int size[l] = { input_l, 64, 32, 26 }; /// 26 ��� ���������� ���� � ���������� ��������

    network nn; /// ������ ������ ������ neural network

    double input[input_l]; /// ������� �������� ���������

    char rresult; /// ���������� ���������
    double result; /// ����� ������� � ������������ ���������
    double ra = 0; /// ���������� ���������� ������� 
    int maxra = 0; /// ������������ ����������
    int maxraepoch = 0; /// ������������ ���������� ����
    const int n = 26; /// ���������� �������� ��� �������� ���������
    bool to_study = 0; /// ����� ��� ������� ��������� ��� ��� ������ �������

    cout << "����������� ��������? (1/0) ";
    cin >> to_study;

    double time = 0;
    if (to_study)
    {

        nn.setLayers(l, size); /// ������� ���� 
        for (int e = 0; ra / n * 100 < 100; e++) /// ���� ��� �� ��� ���, ���� ���������� ������� �� ������ 100% 
        {
            /// cout << "Epoch #" << e << endl;
            fout << "Epoch #" << e << endl;
            double epoch_start = clock(); /// ������� ������� ������ �����
            ra = 0;
            double w_delta = 0;

            fin.open("lib.txt");

            for (int i = 0; i < n; i++)
            {
                double start = clock();
                for (int j = 0; j < input_l; j++)
                {
                    fin >> input[j];
                }
                fin >> rresult;
                double stop = clock();
                time += stop - start;
                rresult -= 65;
                /// cout << int(rresult) << endl;
                /// cout << "����� " << rresult << endl;
                nn.set_input(input);

                result = nn.ForwardFeed();
                /// nn.show();
                if (result == rresult)
                {
                    /// cout << "��������� ������!\n";
                    cout << "������ ����� " << char(rresult + 65) << "\t\t\t****" << endl;
                    ra++; /// ����������� �� ������� ���������� �����
                }
                else
                {
                    /// cout << "��������� " << result << " ��������!\n";
                    /// cout << "�� ������ ����� " << rresult << "\n";
                    nn.BackPropogation(result, rresult, 0.1);
                    /// cout << "BackPropogation time: " << BP_stop - BP_start << endl;
                }
            }
            fin.close();
            double epoch_stop = clock(); /// ������������, ����� ����������� �����
            cout << "Right answers: " << ra / n * 100 << "% \t Max RA: " << double(maxra) / n * 100 << "(epoch " << maxraepoch << " )" << endl;
            /// fout << "Right answers: " << ra / n * 100 << "% \t Max RA: " << double(maxra) / n * 100 << "(epoch " << maxraepoch << " )" << endl;
            cout << "Time needed to fin: " << time / 1000 << " ms\t\t\tEpoch time: " << epoch_stop - epoch_start << endl;
            time = 0;
            /// cout << "W_Delta: " << w_delta << endl;
            if (ra > maxra)
            {
                maxra = ra;
                maxraepoch = e;
            }
            if (maxraepoch < (e - 250))
            {
                maxra = 0;
            }
        }
        fin.close();
        if (nn.SaveWeights()) /// ��������� ����, ���� ���������� ������ ����� 100%
        {
            cout << "���� ���������!";
        }
    }

    else
    {
        nn.setLayersNotStudy(l, size, "weights.txt");
    }
    fin.close();

    cout << "������ ����: (1/0) ";
    bool to_start_test = 0;
    cin >> to_start_test;
    if (to_start_test)
    {
        fin.open("test.txt");
        for (int i = 0; i < input_l; i++)
        {
            fin >> input[i];
        }
        nn.set_input(input);
        result = nn.ForwardFeed();
        cout << "� ������, ��� ��� ����� " << char(result + 65) << "\n\n";
    }

    fin.close();

    return 0;
}
