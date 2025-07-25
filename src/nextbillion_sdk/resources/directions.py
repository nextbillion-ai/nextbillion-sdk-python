# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import direction_compute_route_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.direction_compute_route_response import DirectionComputeRouteResponse

__all__ = ["DirectionsResource", "AsyncDirectionsResource"]


class DirectionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DirectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/nextbillion-sdk-python#accessing-raw-response-data-eg-headers
        """
        return DirectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DirectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/nextbillion-sdk-python#with_streaming_response
        """
        return DirectionsResourceWithStreamingResponse(self)

    def compute_route(
        self,
        *,
        destination: str,
        origin: str,
        waypoints: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DirectionComputeRouteResponse:
        """
        Directions API is a service that computes a route with given coordinates.

        Args:
          destination: test

          origin: test

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/directions/json",
            body=maybe_transform(
                {
                    "destination": destination,
                    "origin": origin,
                    "waypoints": waypoints,
                },
                direction_compute_route_params.DirectionComputeRouteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DirectionComputeRouteResponse,
        )


class AsyncDirectionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDirectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/nextbillion-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDirectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDirectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/nextbillion-sdk-python#with_streaming_response
        """
        return AsyncDirectionsResourceWithStreamingResponse(self)

    async def compute_route(
        self,
        *,
        destination: str,
        origin: str,
        waypoints: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DirectionComputeRouteResponse:
        """
        Directions API is a service that computes a route with given coordinates.

        Args:
          destination: test

          origin: test

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/directions/json",
            body=await async_maybe_transform(
                {
                    "destination": destination,
                    "origin": origin,
                    "waypoints": waypoints,
                },
                direction_compute_route_params.DirectionComputeRouteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DirectionComputeRouteResponse,
        )


class DirectionsResourceWithRawResponse:
    def __init__(self, directions: DirectionsResource) -> None:
        self._directions = directions

        self.compute_route = to_raw_response_wrapper(
            directions.compute_route,
        )


class AsyncDirectionsResourceWithRawResponse:
    def __init__(self, directions: AsyncDirectionsResource) -> None:
        self._directions = directions

        self.compute_route = async_to_raw_response_wrapper(
            directions.compute_route,
        )


class DirectionsResourceWithStreamingResponse:
    def __init__(self, directions: DirectionsResource) -> None:
        self._directions = directions

        self.compute_route = to_streamed_response_wrapper(
            directions.compute_route,
        )


class AsyncDirectionsResourceWithStreamingResponse:
    def __init__(self, directions: AsyncDirectionsResource) -> None:
        self._directions = directions

        self.compute_route = async_to_streamed_response_wrapper(
            directions.compute_route,
        )
