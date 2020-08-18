$(".pop").on("click", function () {
  var dr_ = document.getElementById("reservation").value;
  req = $.ajax({
    url: "/background_process_test",
    type: "POST",
    data: { position: "p", url: "ur" },
  });

  req.done(function (data) {
    alert(data.position);
    $("#divx").remove();
  });
});

$(document).ready(function () {
  $("select").change(function () {
    var element = document.getElementById("search").value;
    var text = $(this).val();
    var X = element + text;
    $(".content").hide(1000);
    $('.content:contains("' + X + '")').show(10000);
  });
});
$(document).ready(function () {
  $("#search").keyup(function () {
    //$((document.getElementById("text-search").value = ""));
    // Search text
    var text = $(this).val();
    $(".content").show();
  });
});

$(document).ready(function () {
  $("#search").keyup(function () {
    // Search text
    var text = $(this).val();

    // Hide all content class element
    $(".content").hide();

    // Search and show
    $('.content:contains("' + text + '")').show();
    $('.content:contains("' + text.toLowerCase() + '")').show(10000);
    $('.content:contains("' + text.toUpperCase() + '")').show(10000);
    $('.content:contains("' + text + '")').show(10000);
  });
});

//rapihin
$(document).on("keyup", ".search-table", function () {
  var value = $(this).val();
  $("table tr").each(function (index) {
    $row = $(this);
    $row.show();
    //if (value) {
    if (index !== 10 && value) {
      var found = false;
      $row.find("td").each(function () {
        var cell = $(this).text();
        if (cell.indexOf(value.toLowerCase() || cell.indexOf(value)) >= 0) {
          found = true;
          return;
        }
      });
      if (found === true) {
        $row.show();
      } else {
        $row.hide();
      }
    }
  });
});

jQuery.fn.highlight = function (pat) {
  function innerHighlight(node, pat) {
    var skip = 0;
    if (node.nodeType == 3) {
      var pos = node.data.toUpperCase().indexOf(pat);
      if (pos >= 0) {
        var spannode = document.createElement("span");
        spannode.className = "highlight";
        var middlebit = node.splitText(pos);
        var endbit = middlebit.splitText(pat.length);
        var middleclone = middlebit.cloneNode(true);
        spannode.appendChild(middleclone);
        middlebit.parentNode.replaceChild(spannode, middlebit);
        skip = 1;
      }
    } else if (
      node.nodeType == 1 &&
      node.childNodes &&
      !/(script|style)/i.test(node.tagName)
    ) {
      for (var i = 0; i < node.childNodes.length; ++i) {
        i += innerHighlight(node.childNodes[i], pat);
      }
    }
    return skip;
  }
  return this.each(function () {
    innerHighlight(this, pat.toUpperCase());
  });
};

jQuery.fn.removeHighlight = function () {
  function newNormalize(node) {
    for (
      var i = 0, children = node.childNodes, nodeCount = children.length;
      i < nodeCount;
      i++
    ) {
      var child = children[i];
      if (child.nodeType == 1) {
        newNormalize(child);
        continue;
      }
      if (child.nodeType != 3) {
        continue;
      }
      var next = child.nextSibling;
      if (next == null || next.nodeType != 3) {
        continue;
      }
      var combined_text = child.nodeValue + next.nodeValue;
      new_node = node.ownerDocument.createTextNode(combined_text);
      node.insertBefore(new_node, child);
      node.removeChild(child);
      node.removeChild(next);
      i--;
      nodeCount--;
    }
  }

  return this.find("span.highlight")
    .each(function () {
      var thisParent = this.parentNode;
      thisParent.replaceChild(this.firstChild, this);
      newNormalize(thisParent);
    })
    .end();
};

$(function () {
  $("#search").bind("keyup change", function (ev) {
    // pull in the new value
    var searchTerm = $(this).val();

    // remove any old highlighted terms
    $("table").removeHighlight();

    // disable highlighting if empty
    if (searchTerm) {
      // highlight the new term
      $("table").highlight(searchTerm);
    }
  });
});
$(function () {
  $("#text-search").bind("keyup change", function (ev) {
    // pull in the new value
    var searchTerm = $(this).val();

    // remove any old highlighted terms
    $("table").removeHighlight();

    // disable highlighting if empty
    if (searchTerm) {
      // highlight the new term
      $("table").highlight(searchTerm);
    }
  });
});
//
//
//
//
//
//
//
//
//
//For Comma's Sparated Value
$(document).ready(function () {
  $("#input_").keyup(function (event) {
    // skip for arrow keys
    if (event.which >= 37 && event.which <= 40) {
      event.preventDefault();
    }
    var $this = $(this);
    var num = $this.val().replace(/,/gi, "").split("").reverse().join("");

    var num2 = RemoveRougeChar(
      num
        .replace(/(.{3})/g, "$1,")
        .split("")
        .reverse()
        .join("")
    );

    console.log(num2);

    // the following line has been simplified. Revision history contains original.
    $this.val(num2);
  });
});

function RemoveRougeChar(convertString) {
  if (convertString.substring(0, 1) == ",") {
    return convertString.substring(1, convertString.length);
  }
  return convertString;
}
