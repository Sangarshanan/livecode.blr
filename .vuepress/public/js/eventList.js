function waitForElements(selector) {
    return new Promise(resolve => {
        if (document.querySelectorAll(selector).length > 0) {
            return resolve(document.querySelectorAll(selector));
        }

        const observer = new MutationObserver(mutations => {
            if (document.querySelectorAll(selector).length > 0) {
                resolve(document.querySelectorAll(selector));
                observer.disconnect();
            }
        });

        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
    });
}

function waitForElement(selector) {
    return new Promise(resolve => {
        if (document.querySelector(selector)) {
            return resolve(document.querySelector(selector));
        }

        const observer = new MutationObserver(mutations => {
            if (document.querySelector(selector)) {
                resolve(document.querySelector(selector));
                observer.disconnect();
            }
        });

        observer.observe(document.body, {
            childList: true,
            subtree: true
        });
    });
}

async function updateEventsPageList() {
  const upcomingEvents = Array.from(await waitForElements("#upcomingEvents > a"));
  const pastEventsDiv = await waitForElement("#pastEvents");

  let notUpcoming = upcomingEvents.filter((e) => {
    return new Date() > new Date(e.querySelector('.date').innerText)
  });

  notUpcoming.forEach((e) => {
    e.parentElement.removeChild(e);
    pastEventsDiv.insertBefore(e, pastEventsDiv.firstChild);
  });
}

async function updateIndexEventsList() {
  const eventsUl = await waitForElement("#events");

  // Remove past events
  eventsUl.querySelectorAll('li').forEach((e) => {
      if (new Date() > new Date(e.innerText)) {
          eventsUl.removeChild(e);
      }
  });

  // Limit list to 4 elements
  Array.from(eventsUl.querySelectorAll('li')).slice(4).forEach((e) => {
      eventsUl.removeChild(e)
  });

  if (eventsUl.querySelectorAll('li').length === 0) {
    const noItemsLi = document.createElement("li")
    noItemsLi.textContent = "No upcoming events";
    noItemsLi.style = "list-style-type: none;";
    eventsUl.appendChild(noItemsLi);
  }
}
