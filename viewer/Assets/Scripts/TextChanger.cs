using System.Collections;
using System.Collections.Generic;
using Unity.Collections.LowLevel.Unsafe;
using UnityEngine;
using UnityEngine.UI;
//using IronPython.Hosting;
using System.IO;

public class TextChanger : MonoBehaviour
{
    public Text textField;

    [SerializeField] private string[,] texts = new string[3,3] { { "PNC-24A", "PNC-24C", "PNC-24D" }, { "Paper", "Balsa Wood", "Clear Plastic" }, { "Estes D12", "Estes E12", "Estes E9" } };


    public int type; // 0 == nose, 1 == body, 2 == engine

    private int textNum;

    public void changeText() 
    {
        textNum++;

        if (textNum > 2)
        {
            textNum = 0;
        }

        textField.text = texts[type, textNum];
    }

    private void Start()
    {
        textField.text = texts[type,0];

        //var engine = Python.CreateEngine();

        //ICollection<string> searchPaths = engine.GetSearchPaths();

        //Path to the folder of greeter.py
        //searchPaths.Add(Directory.GetCurrentDirectory());
        //Path to the Python standard library
        //searchPaths.Add(Directory.GetCurrentDirectory() + @"\Assets\Plugins\Lib\");
        //engine.SetSearchPaths(searchPaths);

        //dynamic py = engine.ExecuteFile(@"C:\Users\jstai\Documents\GitHub\RocketSim\viewer\Assets\Scripts\pythonTest.py");
        //dynamic greeter = py.Greeter("Mika");
        //Debug.Log(greeter.greet());

    }
}
