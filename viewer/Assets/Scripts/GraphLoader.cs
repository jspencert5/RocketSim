using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;
using static UnityEngine.UIElements.UxmlAttributeDescription;
using UnityEngine.PlayerLoop;
using UnityEngine.UI;

public class GraphLoader : MonoBehaviour
{

    public string imagePath;
    public RawImage rawImage;

    void Start()
    {
        Texture2D texture = LoadImage(imagePath);
        rawImage.texture = texture;
    }
    
    Texture2D LoadImage(string path)
    {
        Texture2D texture = new Texture2D(2, 2);
        byte[] imageData = File.ReadAllBytes(path);
        texture.LoadImage(imageData);

        return texture;
    }
}
