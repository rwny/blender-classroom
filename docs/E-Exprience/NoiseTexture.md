# Noise Texture

<!-- Add content here -->
Add > Texture > Noise Texture :
![](./images/noiseTexture953.png "Noise Texture" )

# input
  - 1 2 3 4D
  - texture mode
  - [] Normalize
  - Vector
  - Scale
  - Detail
  - Roughness
  - Lacunarity
  - Distortion
# output
  - Fac
        จะให้ค่า 0.0-1.0 โดยที่ 0 จะแสดงให้เห็นเป็นสีดำ และ 1 จะแสดงให้เห็นเป็นสีขาว ตัวเลขระหว่างนั้น ก็จะเป็นสีเทา ไล่เชดไปจาก 0 ถึง 1
        ** ความจริง ตัวเลขที่ได้ สามารถนำไปแปลงเพื่อให้ค่าน้อยกว่า 0 หรือ มากกว่า 1 ก็ได้ แต่สีที่ให้ออกมาก็มีแค่ ดำ >> ขาว**
    ![](./images/noiseTexture955.png "Noise Texture" )

  - Color จะให้ค่า 0.0-1.0 เหมือนเดิม แต่คราวนี้จะให้มี 3 ช่องทาง เลย คือ Red Green Blue 
  
    ![q](./images/noiseTexture959.png "Noise Texture" )

    สามารถแยกได้โดย Saperate Color

    ![x](./images/noiseTexture956.png "Noise Texture" )
    
    - ในแต่ละช่องสี R G B จะให้ค่า 0-1 เหมือนกัน แต่ตำแหน่งลวดลาย ต่างกัน

