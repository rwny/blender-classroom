# 1.1 What is Blender Geometry Nodes

**Blender Geometry Nodes** คือระบบ **node-based procedural modeling** ที่อยู่ภายใน Blender  
ช่วยให้ผู้ใช้สามารถสร้างและปรับเปลี่ยนโมเดล 3D แบบไม่ทำลายต้นฉบับ (non-destructive)  
โดยใช้การเชื่อมต่อของ nodes แทนการแก้ไขวัตถุด้วยมือแบบดั้งเดิม

## ภาพรวมการทำงาน

- ข้อมูลจะไหลจาก **Input Node → Processing Nodes → Output Node**
- มี node สำหรับการจัดการ:
  - Mesh
  - Curve
  - Point Cloud
  - Instance
  - Material และอื่น ๆ
- สนับสนุนระบบ **Fields** ซึ่งทำให้สามารถประมวลผลข้อมูลแบบไดนามิก เช่น:
  - Noise
  - Distance
  - Selection Logic
- รองรับการใช้ **Attribute** ในการควบคุมค่าต่าง ๆ เช่น:
  - สี
  - ขนาด
  - ตำแหน่ง

## จุดเด่นของ Geometry Nodes

- ทำงานแบบ **parametric และ reusable**
- เหมาะสำหรับ:
  - การสร้าง pattern ที่ซับซ้อน
  - การสร้าง procedural environment
  - งาน motion graphic และการจำลองโครงสร้าง
- ผสานกับระบบอื่นของ Blender ได้ดี เช่น:
  - Modifier Stack
  - Animation
  - Shading

## ตัวอย่างการใช้งาน

- สร้างลวดลายกระเบื้องแบบซ้ำ (tiling pattern)
- สร้างสถาปัตยกรรมด้วย volume logic
- จำลองพื้นผิวที่เกิดจากสูตรคณิตศาสตร์
- กระจายวัตถุแบบสุ่ม (scattering)

## สรุป

Blender Geometry Nodes เปรียบเสมือนระบบ **visual programming** สำหรับการสร้างและจัดการโมเดล 3D  
ให้ความยืดหยุ่นสูง เหมาะกับ workflow แบบ non-destructive และสามารถขยายเป็นระบบที่ซับซ้อนได้ง่าย  
นักออกแบบและนักพัฒนา 3D สามารถใช้มันเพื่อสร้างผลงานอย่างมีโครงสร้าง พร้อมปรับแก้ได้ตลอดเวลา
