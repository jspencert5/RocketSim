using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class TextChanger : MonoBehaviour
{
    public Text textField;

    [SerializeField] private string[,] texts = new string[3,3] { { "PNC-24A", "PNC-24C", "PNC-24D" }, { "Paper", "Fiberglass", "Clear Plastic" }, { "Estes D12", "Estes E12", "Estes E9" } };


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
    }
}
