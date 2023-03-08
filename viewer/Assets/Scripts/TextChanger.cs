using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class TextChanger : MonoBehaviour
{
    public Text textField;

    [SerializeField] private string[] texts;
    private int textNum;

    public void changeText() 
    {
        textNum++;

        if (textNum > texts.Length - 1)
        {
            textNum = 0;
        }

        textField.text = texts[textNum];
    }
}
