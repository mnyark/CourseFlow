function init() {
  const $ = go.GraphObject.make; // for conciseness in defining templates

  const diagram = $(
    go.Diagram,
    "diagram", // create a Diagram for the DIV HTML element
    {
      // automatically scale the diagram to fit the viewport's size
      initialAutoScale: go.Diagram.Uniform,
      // start everything in the middle of the viewport
      initialContentAlignment: go.Spot.Top,
      // position all of the nodes and route all of the links
      layout: $(go.LayeredDigraphLayout, {
        direction: 90,
        layerSpacing: 10,
        columnSpacing: 15,
        setsPortSpots: false
      })
    }
  );

  diagram.addDiagramListener("ObjectSingleClicked", function(e) {
    var part = e.subject.part;
    // alert(part.data.description);
    let p = document.getElementById("courseflow");
    p.innerText = part.data.description;
  });

  diagram.linkTemplate = $(
    go.Link, // the whole link panel
    { curve: go.Link.Bezier, toShortLength: 2 },
    $(
      go.Shape, // the link shape
      { strokeWidth: 1.5 }
    ),
    $(
      go.Shape, // the arrowhead
      { toArrow: "Standard", stroke: null }
    )
  );

  // define a simple Node template
  diagram.nodeTemplate = $(
    go.Node,
    "Auto", // the Shape will go around the TextBlock
    $(
      go.Shape,
      "RoundedRectangle",
      { strokeWidth: 0, fill: "white" },
      // Shape.fill is bound to Node.data.color
      new go.Binding("fill", "color")
    ),
    $(
      go.TextBlock,
      { margin: 10 }, // some room around the text
      // TextBlock.text is bound to Node.data.key
      new go.Binding("text", "key")
    )
  );

  // but use the default Link template, by not setting Diagram.linkTemplate

  // create the model data that will be represented by Nodes and Links
  diagram.model = new go.GraphLinksModel(
    [
      {
        key: "ASTR 1101",
        color: "orange",
        description: "Fundamental prinicples of ASTR 1101."
      },
      {
        key: "ASTR 1102",
        color: "red",
        description: "Fundamental principles of ASTR 1102."
      },
      {
        key: "Modern Observational Techniques",
        color: "lightgreen",
        description:
          "Modern astronomical observations and reductions; the telescope, astronomical photography, spectroscopic and photoelectric observations and reductions."
      },
      {
        key: "Introduction to Data Science",
        color: "yellow",
        description: "random shit"
      },
      {
        key: "Introduction to Data Science 2",
        color: "purple",
        description: "random shit 2"
      },
      {
        key: "Introduction to Data Science 3",
        color: "purple",
        description: "random shit 3"
      }
    ],
    [
      { from: "ASTR 1101", to: "ASTR 1102" },
      { from: "ASTR 1101", to: "Delta" },
      {
        from: "Modern Observational Techniques",
        to: "Introduction to Data Science"
      },
      { from: "Introduction to Data Science", to: "ASTR 1101" },
      { from: "ASTR 1101", to: "Introduction to Data Science 2" },
      { from: "ASTR 1101", to: "Introduction to Data Science 3" }
    ]
  );
}
