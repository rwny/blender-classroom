import os
import sys
import time

# Base directory - use absolute path to ensure clarity
base_dir = os.path.abspath("c:\\Work\\b3d\\_study\\github\\b3d-classroom\\docs")

# File structure from mkdocs.yml
file_paths = [
    # A-Fundamentals
    "A-Fundamentals/1.1-what-is-geometry-nodes.md",
    "A-Fundamentals/1.2-getting-started.md",
    "A-Fundamentals/1.3-components-overview.md",
    "A-Fundamentals/1.4-fields-and-attributes.md",
    "A-Fundamentals/1.5-interface-basics.md",
    "A-Fundamentals/1.6-data-flow.md",
    "A-Fundamentals/1.7-data-structures.md",
    "A-Fundamentals/1.8-curve-surface.md",
    "A-Fundamentals/1.9-mesh-basics.md",
    "A-Fundamentals/1.10-reuse-nodegroups.md",
    "A-Fundamentals/1.11-python-basics.md",
    
    # B-Geometry
    # Tiling
    "B-Geometry/Tiling/tile-pattern-1.md",
    "B-Geometry/Tiling/tile-pattern-2.md",
    "B-Geometry/Tiling/tile-pattern-3.md",
    "B-Geometry/Tiling/hexagonal-puzzle.md",
    # Agents
    "B-Geometry/Agents/point-attractor-1.md",
    "B-Geometry/Agents/point-attractor-2.md",
    "B-Geometry/Agents/curve-attractor.md",
    "B-Geometry/Agents/vector-field.md",
    # Formulas
    "B-Geometry/Formulas/spiral.md",
    "B-Geometry/Formulas/ripple.md",
    "B-Geometry/Formulas/fibonacci.md",
    "B-Geometry/Formulas/fractal-tree.md",
    # Random
    "B-Geometry/Random/wave-surface.md",
    "B-Geometry/Random/gradational-random.md",
    "B-Geometry/Random/drape.md",
    "B-Geometry/Random/random-wire.md",
    # Remapping
    "B-Geometry/Remapping/geometry-remapping.md",
    "B-Geometry/Remapping/pattern-remapping.md",
    "B-Geometry/Remapping/image-remapping.md",
    "B-Geometry/Remapping/text-remapping.md",
    
    # C-Form
    # Aggregating
    "C-Form/Aggregating/brick-wall.md",
    "C-Form/Aggregating/block.md",
    "C-Form/Aggregating/bird-nest.md",
    "C-Form/Aggregating/pine-cone.md",
    # Framing
    "C-Form/Framing/waffle.md",
    "C-Form/Framing/contour.md",
    "C-Form/Framing/weaving.md",
    "C-Form/Framing/geodesic-dome.md",
    # Tessellating
    "C-Form/Tessellating/shell.md",
    "C-Form/Tessellating/gouge.md",
    "C-Form/Tessellating/pyramid.md",
    "C-Form/Tessellating/bubble.md",
    # Mesh
    "C-Form/Mesh/mesh-subdivision.md",
    "C-Form/Mesh/chained-tile.md",
    "C-Form/Mesh/metaball.md",
    "C-Form/Mesh/isosurface.md",
    # Drawing
    "C-Form/Drawing/2d-cut.md",
    "C-Form/Drawing/section.md",
    "C-Form/Drawing/text-label.md",
    "C-Form/Drawing/make-2d.md",
    
    # D-Simulation (fixed from C-Simulation)
    # Physics
    "D-Simulation/Physics/tensile-fabric.md",
    "D-Simulation/Physics/inflated-structure.md",
    "D-Simulation/Physics/origami.md",
    "D-Simulation/Physics/differential-growth.md",
    # Optimization
    "D-Simulation/Optimization/circle-packing.md",
    "D-Simulation/Optimization/panel-optimization.md",
    "D-Simulation/Optimization/solar-radiation.md",
    "D-Simulation/Optimization/remeshing.md",
    # Bridging
    "D-Simulation/Bridging/building-map.md",
    "D-Simulation/Bridging/spreadsheet.md",
    "D-Simulation/Bridging/revit.md",
    "D-Simulation/Bridging/osc.md",
    # Python
    "D-Simulation/Python/sine-hat.md",
    "D-Simulation/Python/recursive-plant.md",
    "D-Simulation/Python/cloud-ribbon.md",
    "D-Simulation/Python/needle-mesh.md"
]

def create_file_structure():
    print(f"Starting file structure creation at: {base_dir}")
    print(f"Current working directory: {os.getcwd()}")
    
    # Check if base directory exists or can be created
    try:
        if not os.path.exists(base_dir):
            print(f"Base directory doesn't exist. Creating: {base_dir}")
            os.makedirs(base_dir, exist_ok=True)
            if os.path.exists(base_dir):
                print(f"✅ Successfully created base directory: {base_dir}")
            else:
                print(f"❌ Failed to create base directory even after attempt")
                return
        else:
            print(f"✅ Base directory already exists: {base_dir}")
    except Exception as e:
        print(f"❌ Error creating base directory: {e}")
        return
    
    files_created = 0
    dirs_created = 0
    
    for file_path in file_paths:
        try:
            # Create full path
            full_path = os.path.join(base_dir, file_path)
            abs_path = os.path.abspath(full_path)
            
            # Get directory from path
            directory = os.path.dirname(abs_path)
            
            # Create directories if they don't exist
            if not os.path.exists(directory):
                os.makedirs(directory, exist_ok=True)
                if os.path.exists(directory):
                    print(f"✅ Created directory: {directory}")
                    dirs_created += 1
                else:
                    print(f"❌ Failed to create directory: {directory}")
            
            # Create the file with a basic template if it doesn't exist
            if not os.path.exists(abs_path):
                with open(abs_path, "w", encoding="utf-8") as f:
                    # Extract title from filename
                    title = os.path.basename(file_path).replace('.md', '').replace('-', ' ').title()
                    
                    # Write a basic markdown template
                    f.write(f"# {title}\n\n")
                    f.write("<!-- Add content here -->\n\n")
                    f.write("## Overview\n\n")
                    f.write("## Examples\n\n")
                    f.write("## Related Topics\n\n")
                
                if os.path.exists(abs_path):
                    print(f"✅ Created file: {abs_path}")
                    files_created += 1
                else:
                    print(f"❌ Failed to create file: {abs_path}")
        except Exception as e:
            print(f"❌ Error processing {file_path}: {e}")
    
    print("\n===== SUMMARY =====")
    print(f"Directories created: {dirs_created}")
    print(f"Files created: {files_created}")
    print(f"Base directory path: {base_dir}")
    print(f"To verify files, check this location in File Explorer: {base_dir}")
    print("====================\n")

if __name__ == "__main__":
    try:
        create_file_structure()
        print("\nScript completed. Press Enter to exit...")
        input()  # Wait for user to press Enter
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("\nScript failed. Press Enter to exit...")
        input()  # Wait for user to press Enter
        sys.exit(1)
